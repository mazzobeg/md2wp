import requests, logging, base64, tabulate, os
from md2wp.mdparser import WPPostParser

class WP_REST_API : 
    POSTS = '/wp-json/wp/v2/posts'
    MEDIA = '/wp-json/wp/v2/media'
   
    def getUrl(wpUrl, wpRestAPI):
        return 'https://%s%s' % (wpUrl, wpRestAPI)

class Interactioner :
    
    def __init__(self, venv) -> None:
        self.wpUrl = venv['WP_URL']
        self.username = venv['USERNAME']
        self.password = venv['PASSWORD']

    def getToken(self) :
        credentials = self.username + ':' + self.password
        return  base64.b64encode(credentials.encode()) 

    def getPosts(self) :
        header = {
            'Authorization': 'Basic ' + self.getToken().decode('utf-8'),
        }

        ans = requests.get(
            url = WP_REST_API.getUrl(self.wpUrl, WP_REST_API.POSTS),
            headers=header,
            )
        
        titles = [[x['title']['rendered']] for x in ans.json()]
        print(tabulate.tabulate(titles, ['List of posts titles'], tablefmt="grid"))
        
    def sendPost(self, path) :
        header = {
            'Authorization': 'Basic ' + self.getToken().decode('utf-8'),
        }
        
        wpparser = WPPostParser(path)
        images = wpparser.getImages()

        for imageUrl, imageObject in images.items() :
            renderedUrl = self.sendMedia(os.path.join( os.path.dirname(path), imageUrl))
            wpparser.updateImgUrl(imageObject, renderedUrl)

        datas = {
            'title' :  wpparser.getTitle(),
            'content' : wpparser.getContent()
        }

        ans = requests.post(
            url = WP_REST_API.getUrl(self.wpUrl, WP_REST_API.POSTS),
            headers=header,
            json=datas
            )

        if str(ans.status_code)[0] == '2' :
            logging.info('Success')
        logging.info(ans)

    def sendMedia(self, path) :
        basenameAsStr:str = os.path.basename(path)
        basenameAsList:list = basenameAsStr.split('.')
        extension = basenameAsList[1]

        header = {
            'Authorization': 'Basic ' + self.getToken().decode('utf-8'),
            'Content-Type': f'image/{extension}',
            'Content-Disposition': f'attachment; filename={basenameAsStr}'
        }
        data = open(path, 'rb').read()

        ans = requests.post(
            url = WP_REST_API.getUrl(self.wpUrl, WP_REST_API.MEDIA),
            headers=header,
            data=data
            )

        logging.info(ans)
        return ans.json()['guid']['rendered']
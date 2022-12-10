import markdown2, logging
from bs4 import BeautifulSoup

class WPPostParser :
    PARSER = 'html.parser'
    def __init__(self, path) -> None:
        with open(path, 'r') as f :
            ans = markdown2.markdown(f.read())
            self.soup = BeautifulSoup(ans, WPPostParser.PARSER)

    def getTitle(self) :
        titles = self.soup.h1.contents
        if len(titles) > 1 : 
            logging.warn('More than 1 title detect in file, I will use the first')
        return str(titles[0])

    def getContent(self) : 
        self.soup.h1.decompose()
        return str(self.soup)

    def getImages(self) :
        finded = self.soup.find_all('img')
        return {f['src'] : f for f in finded}

    def updateImgUrl(self, image, newUrl) :
        imageSrc = image.get('src')
        finded = self.soup.find(attrs={'src':imageSrc})
        finded['src'] = newUrl
        finded['class'] = 'aligncenter'
import json, logging, os, argparse, sys
import md2wp.interactions as interactions

def main(args = None) :
    class CMD : 
        LIST = 'list'
        ADD = 'add'
        ADD_PATH = 'path'

    # Init logger
    logging.basicConfig(level='INFO')

    # Load venv 
    venvFilePath = 'venv.json'
    if not os.path.isfile(venvFilePath) :
        raise FileNotFoundError("venv.json file not found")

    # Check venv integrity
    with open(venvFilePath, 'r') as f:
        venv:dict = json.load(f) 
        required_keys = ['WP_URL', 'USERNAME', 'PASSWORD']
        if not all([rk in venv.keys() for rk in required_keys]) :
            raise Exception("Missing required keys in venv.json")

    # Init interactioner
    interactioner = interactions.Interactioner(venv)

    # Set CLI interface 
    parser = argparse.ArgumentParser()    
    subparsers = parser.add_subparsers(dest='subparserName')
    listPostsSubParser = subparsers.add_parser(CMD.LIST)
    addPostSubParser = subparsers.add_parser(CMD.ADD)
    addPostSubParser.add_argument(CMD.ADD_PATH)
    args = parser.parse_args()

    # Parse arguments
    if args.subparserName == CMD.LIST : 
        interactioner.getPosts()
    if args.subparserName == CMD.ADD : 
        interactioner.sendPost(args.__dict__[CMD.ADD_PATH])

if __name__ == '__main__' : 
    sys.exit( main() )

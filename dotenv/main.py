import requests
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def get_posts(session, id):
    url = f"{os.getenv('api_url')}/posts/{id}"
    r = session.get(url)
    return r.json()

def main():
    configure()
    s = requests.Session()
    firstPost = get_posts(s, 1)
    print(firstPost)

main()

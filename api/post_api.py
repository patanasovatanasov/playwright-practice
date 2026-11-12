import requests

URL_POSTS = "https://jsonplaceholder.typicode.com/posts"
new_post = {"title": "test", "body": "body1", "userId": 1}
r = requests.post(URL_POSTS, json=new_post)

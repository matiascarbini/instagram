import sys
import json
from itertools import islice
from instaloader import Instaloader, Profile

PROFILE = sys.argv[1]

L = Instaloader()

profile = Profile.from_username(L.context, PROFILE)
posts = profile.get_posts()

aPost = []
for post in islice(posts, 8):  
  aPost.append({
    "caption": post.caption,
    "image": post.url,
    "shortcode": "https://instagram.com/p/" + post.shortcode
  })

jsonStr = json.dumps(aPost)

print(jsonStr)
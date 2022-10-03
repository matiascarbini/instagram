from itertools import islice
from math import ceil

from instaloader import Instaloader, Profile

PROFILE = 'mueblestables'

L = Instaloader()

profile = Profile.from_username(L.context, PROFILE)
posts = profile.get_posts()

for post in islice(posts, 8):
  print(post.url)
from twython import Twython
from auth.py import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
    )


twitter = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
    )

# tweet
with open("/home/pi/Desktop/image.jpg", "rb") as photo:
    twitter.upload_media(media=photo)
print("Tweeted")

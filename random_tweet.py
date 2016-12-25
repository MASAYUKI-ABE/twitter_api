import random
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
messages = [
    "Hi, there.",
    "Hello world",
    "What's up?",
    "How's it going?",
    "Have you been here before?",
    "Get a hair cut!"
    ]
message = random.choice(messages)
twitter.update_status(status=message)
print("Tweeted: {}".format(message))

from twython import Twython
from auth import (
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
message = "Hi, there."
twitter.update_status(status=message)
print("Tweeted: {}".format(message))

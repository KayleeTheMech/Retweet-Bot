import datetime
from settings import minimum_account_age
from settings import minimum_account_follower


class RetweetGuard:
    _blocked_ids = []

    def __init__(self, blocked_ids):
        self._blocked_ids = blocked_ids['ids']

    def preliminary_tweet_test(self, tweet):
        # check if user blocked
        if tweet.user.id in self._blocked_ids:
            return False

        # check user for age (bar all younger than <M days)
        account_age = datetime.datetime.now() - tweet.user.created_at
        if account_age.days < minimum_account_age:
            #print("User too young")
            return False

        # check user for follower count (bar everyone with less than N followers)
        if tweet.user.followers_count < minimum_account_follower:
            #print("User too little followers")
            return False

        # okay passed preliminary checks
        return True
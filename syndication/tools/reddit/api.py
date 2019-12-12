import os

import praw


class RedditAPI(object):

    def __init__(self):
        self.reddit_client = praw.Reddit(client_id=os.getenv('REDDIT_CLIENT_ID'),
                                         client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
                                         user_agent='osx:syndicator:0.1 (by /u/aagnone)',
                                         username=os.getenv('REDDIT_USERNAME'),
                                         password=os.getenv('REDDIT_PASSWORD'))

    def post(self, body, matter, publish=False):
        results = {}
        platforms = matter.get('platforms', {})
        subreddit_names = platforms.get(self.name, [])
        for name in subreddit_names:
            sr = self.reddit_client.subreddit(name)
            try:
                submission = sr.submit(
                    body['title'],
                    url=body['canonical_url'])
                results[name] = "Success"
            except Exception:
                import traceback
                traceback.print_exc()
                results[name] = "Fail"

        for name, result in results.items():
            print('%8s %s' % (result, name))

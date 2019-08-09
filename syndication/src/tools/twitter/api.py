import os

import twitter


class Update(object):

    def __init__(self, title, url):
        self.title = title
        self.url = url

    @property
    def text(self):
        return '{} {}'.format(self.title, self.url)


class TwitterAPI(object):

    def __init__(self):
        self.api = twitter.Api(
            consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
            consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
            access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
            access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET']
        )
        self.api.VerifyCredentials()

    def post(self, body, matter, publish=False, **kwargs):
        update = Update(
            body['title'],
            body['canonical_url']
        )
        status = self.api.PostUpdate(update.text, media=body['cover_image'])
        data = status.AsDict()
        print(data)

        # quick sanity check on the returned status
        # data = response.json()
        # if publish:
        #     if data['publishStatus'] != 'public':
        #         raise ValueError('publishStatus not public, but {}'.format(data['publishStatus']))
        # else:
        #     print('Medium draft successfully posted.')

        return data

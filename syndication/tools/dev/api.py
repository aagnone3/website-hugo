import requests
from os import environ

'''
title:              The title of an article (string, optional)
description:        Description of the article (string, optional)
body_markdown:      The Markdown body, with or without a front matter (string, required)
published:          True if the article should be published right away, defaults to false (boolean, optional)
tags:               A list of tags for the article (array, optional)
series:             The name of the series the article should be published within (string, optional)
organization_id:    Your organization's ID, if you wish to create an article under an organization (string, optional)
main_image:         URL of the image to use as the cover (string, optional)
canonical_url:      canonical URL of the article (string, optional)
'''


class DevAPI(object):

    def __init__(self):
        self.token = environ['DEV_API_TOKEN']
        self.endpoint = environ['DEV_ARTICLES_URL']
        self.headers = {
            'Content-Type': 'application/json',
            'api-key': self.token
        }
        self.session = requests.Session()

    def __check_response(self, response):
        if not response.ok:
            print(response.text)
            raise ValueError('Received status code {} from {}.'.format(response.status_code, response.request))

    def post(self, body, matter, publish=False):
        response = self.session.post(self.endpoint, headers=self.headers, json={
            'title': body['title'],
            'description': matter['summary'],
            'body_markdown': body.content,
            'published': publish,
            'tags': body['tags'],
            # TODO 'series': '',
            # TODO 'organization_id': '',
            'main_image': body['cover_image'],
            'canonical_url': body['canonical_url']
        })
        self.__check_response(response)
        if not publish:
            print('View drafts at https://dev.to/dashboard')
        else:
            print('View published articles at {}'.format(response.json()['url']))

    def get_articles(self):
        response = self.session.get(self.endpoint, headers=self.headers, params={
            'username': 'aagnone3'
        })
        if not response.ok:
            raise ValueError('Received status code {} from GET'.format(response.status_code))
        articles = response.json()
        print(articles)

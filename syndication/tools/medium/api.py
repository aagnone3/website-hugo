import os
import requests


class MediumAPI(object):

    def __init__(self):
        self.token = os.environ['MEDIUM_INTEGRATION_TOKEN']
        self.api_url = os.environ['MEDIUM_API_URL']
        self.api_version = os.environ['MEDIUM_API_VERSION']
        self.session = requests.Session()
        self.session.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(self.token)
        }
        self.endpoint = '{base}/{version}'.format(base=self.api_url, version=self.api_version)
        self.user_id = self.__get_user_id()
        self.publications = self.__get_user_publications(self.user_id)

    def __check_response(self, response):
        if not response.ok:
            print(response.text)
            raise ValueError('Received status code {} from {}.'.format(response.status_code, response.request))

    def __get_user_id(self):
        response = self.session.get('{endpoint}/me'.format(endpoint=self.endpoint))
        self.__check_response(response)
        return response.json()['data']['id']

    def __get_user_publications(self, user_id):
        response = self.session.get('{endpoint}/users/{uid}/publications'.format(
            endpoint=self.endpoint, uid=self.user_id))
        self.__check_response(response)

        return {
            e['name']: e['id']
            for e in response.json().get('data', {})
        }

    def post(self, body, matter, publish=False, **kwargs):
        publication = matter.get('publication', '')
        should_publish = 'public' if publish and publication == '' else 'draft'
        response = self.session.post(
            '{endpoint}/users/{uid}/posts'.format(endpoint=self.endpoint, uid=self.user_id), json={
                'title': body['title'],
                'content': body.content,
                'contentFormat': 'markdown',
                'canonicalUrl': body['canonical_url'],
                'tags': body['tags'].split(','),
                'publishStatus': should_publish,
                # 'publicationId': self.publications.get(publication, ''),
                'notifyFollowers': publish
            })
        self.__check_response(response)

        # quick sanity check on publish status
        data = response.json()
        if publish:
            if data['publishStatus'] != 'public':
                raise ValueError('publishStatus not public, but {}'.format(data['publishStatus']))
        else:
            print('Medium draft successfully posted.')

        return data

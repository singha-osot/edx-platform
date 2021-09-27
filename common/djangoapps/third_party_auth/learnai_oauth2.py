from social_core.backends.oauth import BaseOAuth2


class LearnAIOAuth2(BaseOAuth2):
    name = 'learn-ai'
    AUTHORIZATION_URL = 'http://ai4all.t.innosoft.kmutt.ac.th/oauth2/authorize'
    ACCESS_TOKEN_URL = 'http://ai4all.t.innosoft.kmutt.ac.th/oauth2/access_token'
    ACCESS_TOKEN_METHOD = 'POST'
    STATE_PARAMETER = 1

    def get_user_details(self, response):
        return {'username': response[0].get('username'),
                'fullname': response[0].get('name'),
                'email': response[0].get('email'),
                'profile_image': response[0].get('profile_image')}

    def user_data(self, access_token, *args, **kwargs):
        url = 'http://ai4all.t.innosoft.kmutt.ac.th/api/user/v1/accounts'
        header = {"Authorization": "Bearer %s" % access_token}
        return self.get_json(url, headers=header)

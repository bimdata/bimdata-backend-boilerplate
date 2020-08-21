from rest_framework.authentication import get_authorization_header


class User:
    def __init__(self, access_token, id_token):
        self.access_token = access_token
        self.id_token = id_token
        self.email = id_token.get("email").lower()
        self.first_name = id_token.get("given_name")
        self.last_name = id_token.get("family_name")
        self.sub = id_token.get("sub")
        self.provider = id_token.get("preferred_username").split(".")[0]

    @property
    def is_authenticated(self):
        # hack for compatibility with user permissions
        return True


def get_user_by_id(request, id_token):
    # raw access_token
    access_token = get_authorization_header(request).split()[1].decode("ascii")
    user = User(access_token, id_token)

    return user

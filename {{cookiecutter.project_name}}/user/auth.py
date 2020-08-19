class User:
    def __init__(self, id_token):
        self.id_token = id_token
        self.email = id_token.get("email").lower()
        self.first_name = id_token.get("given_name")
        self.last_name = id_token.get("family_name")
        self.sub = id_token.get("sub")
        self.provider = id_token.get("preferred_username").split('.')[0]


    @property
    def is_authenticated(self):
        # hack for compatibility with user permissions
        return True


def get_user_by_id(request, id_token):
    return User(id_token)

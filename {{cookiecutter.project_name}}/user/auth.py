class User:
    @property
    def is_authenticated(self):
        # hack for compatibility with user permissions
        return True


def get_user_by_id(request, id_token):
    return User()

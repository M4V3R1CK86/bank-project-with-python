class AuthenticationCredentialsModel:
    def __init__(self, user_id, password_hash):
        self.user_id = user_id
        self.password_hash = password_hash

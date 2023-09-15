import bcrypt


class UsersModel:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.salt = bcrypt.gensalt()
        self.password = None

    def set_password(self, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), self.salt)
        # Converta a senha hash (hashed_password) para uma string antes de armazená-la
        self.password = hashed_password.decode('utf-8')

    def check_password(self, password):
        # Verifique se a senha fornecida corresponde à senha hash armazenada usando o salt correto
        stored_password_hash = bcrypt.hashpw(
            password.encode('utf-8'), self.salt)
        return stored_password_hash == self.password.encode('utf-8')

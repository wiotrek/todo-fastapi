from bcrypt import gensalt, hashpw, checkpw


class Hasher:
    @staticmethod
    def verify_password(plain_password: str, hashed_password: any):
        plain_password_byte_enc: bytes = plain_password.encode('utf-8')
        hashed_password_byte_enc: bytes = hashed_password.encode('utf-8')
        return checkpw(password=plain_password_byte_enc, hashed_password=hashed_password_byte_enc)

    @staticmethod
    def get_password_hash(password):
        pwd_bytes = password.encode('utf-8')
        salt = gensalt()
        hashed_password = hashpw(password=pwd_bytes, salt=salt)
        return hashed_password.decode('utf-8')

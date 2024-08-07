import strawberry


@strawberry.type
class TokenType:
    access_token: str
    token_type: str

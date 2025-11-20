import datetime
import typing

from rest_framework_simplejwt.tokens import RefreshToken

from auth_email.models import User


def get_tokens_for_user(
    user: User,
    user_tags: typing.List[str] | None = None,
    lifetime: datetime.timedelta | None = None,
    **claims: typing.Any,
):
    refresh = RefreshToken.for_user(user)
    if user_tags:
        refresh['user_tags'] = user_tags
    for claim, value in claims.items():
        refresh[claim] = value

    access = refresh.access_token
    if lifetime:
        access.set_exp(lifetime=lifetime)

    return {'refresh': str(refresh), 'access': str(access)}

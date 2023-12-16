from rest_framework_jwt.settings import api_settings
import random
import string
from vendor.models.users import User


def jwt_response_payload_handler(token, user, request, *args, **kwargs):
    user = User.objects.get(pk=user.id)
    data = dict(token=token)
    return data

def create_jwt_token(user_obj):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user_obj)
    token = jwt_encode_handler(payload)
    return token

def randomStringDigits(stringLength):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
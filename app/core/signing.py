import hmac
import hashlib
from urllib.parse import urlencode

from app.core.config import settings

def generate_signature(params : dict) -> str:
    query_string = urlencode(sorted(params.items()))
    return hmac.new(settings.SECRET_KEY.encode(),
                    query_string.encode(),
                    hashlib.sha256).hexdigest()

def verify_signature(params : dict, signature : str) -> bool:
    expected = generate_signature(params)
    return hmac.compare_digest(expected,signature)
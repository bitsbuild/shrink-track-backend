import random
import string
from api.models import UniqueCode
used_codes = set()
def generate_unique_code():
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(chars,k=6))
        if not UniqueCode.objects.filter(code=code).exists():
            UniqueCode.objects.create(code=code)
            return code
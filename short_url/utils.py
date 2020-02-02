import random
import string
from .utils2 import randomGenerate



def newCode(instance, size=150):
    new_code = randomGenerate(size=size)

    klass = instance.__class__
    check = klass.objects.filter(shortUrl=new_code).exists()

    if check:
        return newCode(size=size + 1)
    return new_code

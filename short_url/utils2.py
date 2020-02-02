import random
import string
# from .models import content

def randomGenerate(size=150, chars=string.ascii_letters + string.digits):
    randoms = random.randrange(content.objects.all().count())
    slug = list(content.objects.all())
    generate = ''.join(random.choice(chars) for _ in range(size))
    urlFinal = 'https://next.gamebook-powered.xyz/article/' + str(slug[randoms]) + '/' + generate
    return urlFinal

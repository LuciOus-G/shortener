from django.db import models
from .utils import newCode
from django.utils.text import slugify
import random
import string

class content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(default='', blank=True, editable=False)
    image = models.ImageField(default='', upload_to='Thumb')

    def __str__(self):
        return self.slug

    def save(self):
        self.slug = slugify(self.title)
        super(content, self).save()

    def snippet(self):
        return self.body [:100]

class short(models.Model):
    longUrl = models.CharField(max_length=255)
    Token = models.CharField(max_length=255, unique=True, blank=True, editable=False)
    Link = models.CharField(max_length=255, unique=True, blank=True, default='Link', editable=False)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        if self.Token is "":
            self.Token = randomGenerate()
            self.Link = randomGenerate.urlFinal
        super(short, self).save(*args, **kwargs)

    def __str__(self):
        return '{}, {}'.format(self.id, self.longUrl)

    def __unicode__(self):
        return str(self.longUrl)

def randomGenerate(size=150, chars=string.ascii_letters + string.digits):
    randoms = random.randrange(content.objects.all().count())
    slug = list(content.objects.all())
    generate = ''.join(random.choice(chars) for _ in range(size))
    qs = short.objects.filter(Token=generate).exists()
    if qs:
        randomGenerate(size=size + 1)
    randomGenerate.urlFinal = 'https://next.gamebook-powered.xyz/article/' + str(slug[randoms]) + '/' + generate
    return generate

def linkGenerate(size=150, chars=string.ascii_letters + string.digits):
    randoms = random.randrange(content.objects.all().count())
    slug = list(content.objects.all())
    generate = ''.join(random.choice(chars) for _ in range(size))
    qs = short.objects.filter(Token=generate).exists()
    if qs:
        randomGenerate(size=size + 1)
    urlFinal = 'https://next.gamebook-powered.xyz/article/' + str(slug[randoms]) + '/' + generate
    return urlFinal

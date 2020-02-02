from django.contrib import admin
from .models import short, content

# Register your models here.
class link(admin.ModelAdmin):
    readonly_fields = ['Token', 'Link']
class slug(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(short, link)
admin.site.register(content, slug)

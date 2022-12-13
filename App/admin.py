from django.contrib import admin
from . models import Article, Place, Video, Contact, Hotel

# Register your models here.
admin.site.register(Video)
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Hotel)
admin.site.register(Place)


admin.site.site_header = 'Adda Travelling'
admin.site.index_title = 'Adda Travelling'
from django.contrib import admin

# Register your models here.
from bgimage.models import Bgimage

class BgimageAdmin(admin.ModelAdmin):
	list_display=('bg_image','bg_title')
admin.site.register(Bgimage,BgimageAdmin)
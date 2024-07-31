from django.contrib import admin
from .models import document,image,Register,user_info
# Register your models here.
admin.site.register(document)
admin.site.register(image)
admin.site.register(Register)
admin.site.register(user_info)

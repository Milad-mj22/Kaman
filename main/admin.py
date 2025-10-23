from django.contrib import admin

from main.models import Article, BusinessArea, CompanySize, DemoUser

# Register your models here.


admin.site.register(CompanySize)

admin.site.register(BusinessArea)

admin.site.register(DemoUser)
admin.site.register(Article)
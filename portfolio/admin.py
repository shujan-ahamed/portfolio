from django.contrib import admin

from portfolio.models import Achivements, ContactMessages, Education, Experience, Portfolio, Resume, Skills, Languages, Web_cat, Features

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Resume)
admin.site.register(Skills)
admin.site.register(ContactMessages)
admin.site.register(Achivements)

admin.site.register(Languages)
admin.site.register(Web_cat)
admin.site.register(Features)


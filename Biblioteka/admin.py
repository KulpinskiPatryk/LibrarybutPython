from django.contrib import admin
from .models import *


admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Genre)
admin.site.register(Borrowed)
admin.site.register(User_of_Library)

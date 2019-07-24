from django.contrib import admin
from .models import Blog
# 같은 폴더 위치에 있는 models.py의 Blog 클래스를 가져옴.

admin.site.register(Blog)
# admin이라는 site에 Blog라는 클래스를 등록함.






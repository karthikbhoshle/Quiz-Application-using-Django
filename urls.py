from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.index,name='index'),
path('charcount',view.charcount,name='charcount'),
path('quiz',view.quiz,name='quiz'),
path('check',view.check,name='check')
]

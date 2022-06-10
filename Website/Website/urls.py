
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
   # path('AllBooks/',views.booklist.as_view()),
   # path('',include('BookRecords.urls')),
]

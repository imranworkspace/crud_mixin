
from django.contrib import admin
from django.urls import path
from api.views import StudentList,StudentCreate,StudentRetrive


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/',StudentCreate.as_view()),
    path('list/',StudentList.as_view()),
    path('retrive/<int:pk>/',StudentRetrive.as_view()),
]

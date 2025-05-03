from django.contrib import admin
from django.urls import path
from survey import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.survey_form, name='survey_form'),
    path('survey-list/', views.survey_list, name='survey_list'),
]


from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='home'),
    path('WAForm', views.WAForm, name='WAForm'),
    path('grades', views.grades, name='grades'),
    path('SMSForm', views.SMSForm, name='SMSForm'),

]

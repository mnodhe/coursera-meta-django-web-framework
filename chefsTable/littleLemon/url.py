from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name='home'),
    path('newpage/', view=views.new_page),
    path('about/', view=views.about, name='about'),
    path('menu/<int:menu_id>', view=views.menu_by_id, name='menu_by_id'),
    path('sayhello/', view=views.say_hello, name='say_hello'),
    path('index/', view=views.index, name='index'),
    path('reqres/', view=views.reqres, name='reqres'),
    path('form/', view=views.form_view, name='form_view'),
    
]

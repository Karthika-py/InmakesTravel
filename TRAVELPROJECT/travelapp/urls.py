from . import views
from django.urls import path

urlpatterns = [

    # path('', views.index, name='index')
    path('', views.indexplace, name='index')


    # path('',views.objectparameter,name='objectpass')

#     path('',views.home,name='home'),
#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact'),
#     path('details/',views.details,name='details'),
#     path('thanks/',views.thanks,name='thanks')


#     path('',views.index_add,name='add'),
#     path('add/',views.addition,name='addition')


 ]
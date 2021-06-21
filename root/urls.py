
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

 
urlpatterns = [ 
    path('', index, name='index'),  
    path('deletefile/<str:id>', deletefile, name='deletefile'),  
    path('updatefile/<str:id>', updatefile, name='updatefile'),   
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


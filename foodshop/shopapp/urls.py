from django.urls import path
from shopapp import views
from django.conf.urls.static import static 
from foodshop import settings 


urlpatterns = [
   path('index',views.index),
   path('fdetails/<fid>',views.fdetails),
   path('yourcart',views.yourcart),
   path('uregister',views.register),
   path('ulogin',views.ulogin),
   path('ulogout',views.ulogout),
   path('catfilter/<cv>',views.catfilter),
   path('sort/<sv>',views.sort),
   path('range',views.range),
   path('addtocart/<fid>',views.addtocart),
   path('remove/<cid>',views.remove),
   path('updateqty/<qv>/<cid>',views.updateqty),
   path('confirmorder',views.confirmorder),
   path('paynow',views.paynow),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
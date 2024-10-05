from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bkash/', include('bkash.urls')),
    path('',include('store.urls')),
    path('cart/',include('cart.urls')),
    path('author/',include('author.urls')),
    path('payment/',include('payment.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


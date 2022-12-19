"""EtOrder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts import views
from Product.views import order_conform

urlpatterns = [
    path('admin/', admin.site.urls),
    path('repo/', include('reporter.urls')),
    path('product/', include('Product.urls')),
    path('',views.index,name='index'),
    path('order/conformed/', order_conform, name='Product_order_conform'),
    path('accounts/',include('accounts.urls')),
    path('logout/',views.userLogout,name='logout'),
    path('customerDash/',views.customerDash,name='customerDash'),
    path('staffDash/',views.staffDash,name='staffDash'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

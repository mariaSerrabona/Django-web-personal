"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from django.conf import settings


#enlazamos cada elemento creado del views con uns url de la web
urlpatterns = [
    path('', core_views.home, name="base.html"),
    path('about.html/', core_views.about, name="about.html"),
    path('portfolio.html/', core_views.portfolio, name="portfolio.html"),
    path('contact.html/', core_views.contact, name="contact.html"),
    path('admin.html/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
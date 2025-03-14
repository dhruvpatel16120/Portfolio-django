"""
URL configuration for DPO project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Home import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap
from django.views.generic import TemplateView

# Admin Penal
admin.site.site_title = "Dhruv Patel Admin"
admin.site.site_header = "Dhruv Patel Admin"
admin.site.index_title = "Admin Penal"

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin-a/', admin.site.urls),
    path('',views.home,name="home"),
    path('<str:portfolio_name>/',views.portfoliodetails,name="portfoliodetails"),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
]
handler404 = 'Home.views.handling_404'

# Add URL patterns for serving media files during development.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

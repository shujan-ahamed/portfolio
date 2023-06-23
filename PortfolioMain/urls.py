from django.contrib import admin
from django.urls import path, include

from PortfolioMain.views import  contact, home, resume, services


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('dashboard/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    path('secure_admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('resume/', resume, name='resume'),
    #includes
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

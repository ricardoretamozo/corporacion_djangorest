from django.contrib import admin
from django.urls import path,include,re_path
from apps.users.views import Login,Logout,UserToken
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('usuario/',include('apps.users.api.urls')),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('login/',Login.as_view(), name = 'login'),
    path('refresh-token/',UserToken.as_view(), name = 'refresh_token'),
    path('business/', include('apps.business.api.routers')),
    path('client/', include('apps.client.api.routers')),
    path('employee/', include('apps.employee.api.routers')),
    path('products/', include('apps.products.api.routers')),
    path('projects/', include('apps.projects.api.routers')),
    path('reports/', include('apps.reports.api.routers')),
    path('supplies/', include('apps.supplies.api.routers')),
    path('vendors/', include('apps.vendors.api.routers')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
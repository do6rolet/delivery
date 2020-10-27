from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from market.views.index import index

schema_view = get_schema_view(
    openapi.Info(
        title="Delivery API",
        default_version='v1',
        description='''
            Documentation `ReDoc` view can be found [here](/doc)''',
        contact=openapi.Contact(email="do6rolet@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# регистрируем роутер в rest_framework
from rest_framework import routers
from market.views.category import CategoryViewSet
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)



urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('v1/', include([
        path('generic/', include(router.urls)),
        path('market/', include('market.urls'))

    ])),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

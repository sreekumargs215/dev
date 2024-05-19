from django.urls import path
from resumeapp import views
app_name="resumeapp"
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    # path('index/',views.index),
    # path('profile/',views.profile),
    # path('tables/',views.table1),
    # path('dashboard/',views.dashboard),
    # path('icons/',views.icons1),
    # path('forms/',views.forms1),
    # path('register/',views.register),
    path('',views.portfolio),
    # path('',views.login1),
    # path('calender/',views.calender1),
    # path('logout/',views.logoutdata),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 
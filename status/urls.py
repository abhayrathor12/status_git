from django.contrib import admin
from django.urls import path
from status_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.StatusPageFunc, name='StatusPageFunc'),
    path('ReportPageFunc', views.ReportPageFunc, name='ReportPageFunc'),
    path('ReportFunc', views.ReportFunc, name='ReportFunc'),
    path('AnalyticsFunc', views.AnalyticsFunc, name='AnalyticsFunc'),
    path('Emailfunc', views.Emailfunc, name='Emailfunc'),
    path('deleteemail/<int:id>/',views.deleteemail,name='deleteemail'),
    path('TotaltimeFunc', views.TotaltimeFunc, name='TotaltimeFunc'),
    
    
]

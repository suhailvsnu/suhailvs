"""
URL configuration for hospital project.

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
from hosp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('doctor/',views.doctor),
    path('adddoctor/',views.adddoctor),
    path('nurse/',views.nurse),
    path('viewdoctor/',views.adddoctor),
    path('addnurse/',views.addnurse),
    path('doctorview/',views.viewdoctor),
    path('viewnurse/',views.viewnurse),
    path('delnurse/<int:id>',views.delnurse),
    path('deldoc/<int:id>',views.deldoc),
    path('updatenurse/<int:id>',views.updnurse1),
    path('updnurse2/<int:id>',views.updnurse2),
    path('updtdoc1/<int:id>',views.upddoc1),
    path('updtdoc2/<int:id>',views.upddoc2),




]

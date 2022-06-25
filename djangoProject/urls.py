"""djangoProject URL Configuration

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
from . import view,testdb
import index.views as inc

urlpatterns = [
    path("", inc.index),
    path('admin/', admin.site.urls),
    path('index/',inc.index),
    path('hello/',view.hello),
    path('runoob/',view.runoob),
    path('itemsToOrder/',inc.itemToOrder),
    path('testdb01/',testdb.testdbAdd),
    path('testdb02/',testdb.testdbRmv),
    path('test/',inc.btTest),
    path('allitems/',inc.allItems),
    path('item/',inc.itemPage),
    path('test2/',inc.test02),
    path('customer',inc.customer),
    path('orderItem/', inc.orderItem),
    path('loginPage/',inc.loginPage),
    path('login/', inc.login),
    path('createOrder/',inc.createOrder),
    path('orders/',inc.orderPage),
    path('allorders/',inc.allOrder)
]

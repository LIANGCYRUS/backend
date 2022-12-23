# from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from ordersystem.views import AlipayMyTransactionViewSet, TmgListViewSet

# 实例化一个DefaultRouter对象
router = DefaultRouter()

# 注册相对应的url
router.register("alipay", AlipayMyTransactionViewSet, basename='alipay')
router.register("tmg", TmgListViewSet, basename='tmg')

urlpatterns = []

urlpatterns += router.urls

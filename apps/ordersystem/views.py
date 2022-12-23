from django.shortcuts import render
# 封装完整的ModelViewSet视图集合
from rest_framework.viewsets import ModelViewSet
from ordersystem.models import AlipayMyTransaction, TmgList
from ordersystem.serializer import AlipayMyTransactionSerializer, TmgListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ordersystem.filter import AlipayMyTransactionFilter, TmgListFilter


# Create your views here.
class AlipayMyTransactionViewSet(ModelViewSet):
    queryset = AlipayMyTransaction.objects.all()
    serializer_class = AlipayMyTransactionSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_class = AlipayMyTransactionFilter


class TmgListViewSet(ModelViewSet):
    queryset = TmgList.objects.all()
    serializer_class = TmgListSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_class = TmgListFilter

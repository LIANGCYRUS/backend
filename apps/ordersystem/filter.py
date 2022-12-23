from django_filters import FilterSet
from ordersystem.models import AlipayMyTransaction, TmgList


class AlipayMyTransactionFilter(FilterSet):
    class Meta:
        model = AlipayMyTransaction
        fields = ('Partner_transaction_id',)


class TmgListFilter(FilterSet):
    class Meta:
        model = TmgList
        fields = ('Order_id',)

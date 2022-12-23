# 导入模块
from rest_framework import serializers #导入序列化模块
from ordersystem.models import AlipayMyTransaction, TmgList #导入序列化模块


# 支付宝列的序列化
class AlipayMyTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlipayMyTransaction
        fields = "__all__"


# 支付宝列的序列化
class TmgListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TmgList
        fields = "__all__"

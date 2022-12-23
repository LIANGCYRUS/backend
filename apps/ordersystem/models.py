from django.db import models


# Create your models here.

# 国际支付宝页面基准系统的models
class AlipayMyTransaction(models.Model):
    Partner_transaction_id = models.CharField(verbose_name="Partner_transaction_id", max_length=100)
    Transaction_id = models.CharField(verbose_name="Transaction_id", max_length=100, )
    Amount = models.IntegerField(verbose_name="Amount")
    Rmb_amount = models.IntegerField(verbose_name="Rmb_amount")
    Fee = models.IntegerField(verbose_name="Fee")
    Refund = models.IntegerField(verbose_name="Refund")
    Settlement = models.IntegerField(verbose_name="Settlement")
    Rmb_settlement = models.IntegerField(verbose_name="Rmb_settlement")
    Currency = models.CharField(verbose_name="Currency", max_length=100)
    Rate = models.CharField(verbose_name="Rate", max_length=100, )
    Payment_time = models.DateTimeField(verbose_name="Payment_time", max_length=100)
    Settlement_time = models.DateTimeField(verbose_name="Settlement_time", max_length=100)
    Type = models.CharField(verbose_name="Type", max_length=100)

    class Meta:
        managed = True
        app_label = 'ordersystem'
        db_table = 'AlipayOrder'

    # def __str__(self):
    #     return "%s" % (self.Partner_transaction_id)


class TmgList(models.Model):
    Order_id = models.CharField(verbose_name="Order_id", max_length=100)
    Transaction_id = models.CharField(verbose_name="Transaction_id", max_length=100)
    Order_time = models.DateTimeField(verbose_name="Order_time")
    Pay_time = models.DateTimeField(verbose_name="Pay_time")
    Send_time = models.DateTimeField(verbose_name="Send_time")
    Confirm_time = models.DateTimeField(verbose_name="Confirm_time")

    class Meta:
        managed = True
        app_label = 'ordersystem'
        db_table = 'TmgOrder'

    # def __str__(self):
    #     return "%s" % (self.Order_id)

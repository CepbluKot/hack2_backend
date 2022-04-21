import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import managers  # we will write this file shortly


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=50, blank=False)
    departament = models.CharField(max_length=30, blank=True)
    pro = models.BooleanField(default=False)
    telegram_id = models.CharField(max_length=50, blank=False)
    seller = models.ForeignKey('Seller', on_delete=models.CASCADE, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return f"{self.seller.name}"

    class Meta:
        db_table = 'custom_user'


class QuotationSession(models.Model):
    """"
        id name start time, end time, start_price, winner, final_price, percent
    """
    name = models.CharField(max_length=50, blank=False)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)
    reducing_factor = models.DecimalField(max_digits=3, decimal_places=2)
    winner = models.OneToOneField('Seller', on_delete=models.CASCADE, null=True, blank=True, default=None)

    class Meta:
        db_table = 'quotation_session'

    def __str__(self):
        return f"id={self.name}, name={self.name}"


class Seller(models.Model):
    name = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = 'seller'

    def __str__(self):
        return f"name={self.name}"


class ConnectTable(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    session = models.ForeignKey(QuotationSession, on_delete=models.CASCADE)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    auto_status = models.BooleanField(default=False)

    class Meta:
        db_table = 'connect_table'

    def __str__(self):
        return f"Seller: {self.seller.name} / Session: {self.session.name}"


class QSPriceHistory(models.Model):
    """"
        time, change_count, price, Seller
    """
    time = models.DateTimeField(auto_now=True)
    change_cnt = models.IntegerField(blank=True, default=1)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    info = models.ForeignKey(ConnectTable, on_delete=models.CASCADE)

    class Meta:
        db_table = 'qs_price_history'





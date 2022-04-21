from pprint import pprint

from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

import psycopg2

import backEnd.settings
from accounts.serializer import QSPriceHistoryAllSerializer, UserStatusSerializer
from . import serializer
from accounts.models import Seller, QuotationSession, QSPriceHistory, ConnectTable

conn = psycopg2.connect(
    user="dmitri101",
    password="dbpass",
    host="127.0.0.1",
    port="5432",
    database="quotation"
)
cursor = conn.cursor()

CustomUser = get_user_model()


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.SellerSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Seller.objects.all()


class QuotationSessionViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.QuotationSessionSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = QuotationSession.objects.all()


class QuotationSessionAllViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.QuotationSessionAllSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = QuotationSession.objects.all()


class QSPriceHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.QSPriceHistorySerializer
    permission_classes = (permissions.AllowAny,)
    queryset = QSPriceHistory.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = QSPriceHistory.objects.all()
        serializer = QSPriceHistoryAllSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):

        cursor.execute(f"select id, qs_price_history.time, current_price from qs_price_history "
                       f"where info_id = {pk}"
        )
        this_res = cursor.fetchall()
        result = []
        for i in this_res:
            k = []

            cursor.execute(f"select seller.name from qs_price_history "
                           f"join connect_table on connect_table.id = qs_price_history.id"
                           f" join seller on connect_table.id = seller.id "
                           f"where qs_price_history.id = {i[0]}"
                           )
            this_bit = cursor.fetchall()
            k.append(i[1])
            k.append(i[2])
            k.append(this_bit)
            result.append(k)

        # print(result)
        data = []
        for i in result:
            data.append({
                "time": i[0],
                "seller_name": i[2],
                "current_price": i[1]
            })
        return Response(data)


class CustomUserModelViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.CustomUserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class UserStatusViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.UserStatusSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = ConnectTable.objects.all()

    def retrieve(self, request, pk=None, *args, **kwargs):
        cursor.execute(f"select seller_id, seller.name from connect_table join seller on connect_table.seller_id = seller.id where session_id = {pk}")
        all_seller_info = cursor.fetchall()
        print(all_seller_info)

        result_us_in_session = {}
        for one_seller in all_seller_info:
            result_us_in_session[one_seller[0]] = one_seller[1]

        full_result_info = {pk : result_us_in_session}
        return Response({"session": full_result_info})
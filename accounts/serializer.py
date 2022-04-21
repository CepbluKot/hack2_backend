from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
from accounts.models import Seller, QuotationSession, QSPriceHistory, ConnectTable


CustomUser = get_user_model()


class SellerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = Seller
        fields = '__all__'
        

class QuotationSessionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    start_time = serializers.DateTimeField(required=True)
    end_time = serializers.DateTimeField(required=True)
    # winner = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = QuotationSession
        extra_kwargs = {
            'start_price': {'max_digits': 10, 'decimal_places': 2},
            'final_price': {'max_digits': 10, 'decimal_places': 2},
            'reducing_factor': {'max_digits': 10, 'decimal_places': 2},
        }

        fields = ('name', 'start_time', 'end_time', 'start_price', 'final_price', 'reducing_factor', 'winner')


class QuotationSessionAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuotationSession
        # extra_kwargs = {
        #     'start_price': {'max_digits': 10, 'decimal_places': 2},
        #     'final_price': {'max_digits': 10, 'decimal_places': 2},
        #     'reducing_factor': {'max_digits': 10, 'decimal_places': 2},
        # }

        fields = '__all__'
        depth = 2


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message='This email already exists',
            queryset=CustomUser.objects.all()
        )]
    )
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(required=False)
    departament = serializers.CharField(required=False)
    pro = serializers.BooleanField(required=False)
    telegram_id = serializers.CharField(required=False)
    # seller = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        # extra_kwargs = {
        #     'seller': {'source': 'name'},
        # }
        fields = ('name', 'departament', 'email',
                  'password', 'pro', 'telegram_id', 'seller')

        depth= 2

    # def create(self, validated_data):
    #     print(validated_data['seller'])
    #     custom_user = CustomUser.objects.create(
    #
    #     )
    #
    #     return super().create(validated_data)


class QSPriceHistorySerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(read_only=True)
    # change_cnt = serializers.IntegerField()
    current_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    # user = CustomUserSerializer()
    # session = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = QSPriceHistory
        fields = ('id', 'time', 'current_price', 'info')
        # depth = 2


class QSPriceHistoryAllSerializer(serializers.ModelSerializer):
    # history =
    class Meta:
        model = QSPriceHistory
        fields = '__all__'
        depth = 3


class CustomUserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserStatusSerializer(serializers.ModelSerializer):
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = ConnectTable
        fields = '__all__'
        # depth = 2




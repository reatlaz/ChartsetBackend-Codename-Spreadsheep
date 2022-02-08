from rest_framework.fields import SerializerMethodField
from chartsets.models import Chartset
from rest_framework import serializers
from users.serializers import UserSerializer

class ChartsetSerializer(serializers.ModelSerializer):
    #задать вопрос про отображение поля ManyToMany
    userschartsets = UserSerializer(read_only=True, many=True)
    #userschartsets = serializers.CharField(read_only=True)
    #userschartsets = serializers.SerializerMethodField()
    class Meta:
        model = Chartset
        fields = ['id', 'name', 'userschartsets', 'date_modified']
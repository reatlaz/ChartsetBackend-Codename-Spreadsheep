from users.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    #задать вопрос про отображение поля ManyToMany
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
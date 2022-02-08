from django.conf import settings
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import User

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'usr'

    settings = {
        'number_of_shards': 1,
        'number_of replicas': 0

    }

    class Django:
        model = User
        fields = [
            'username',
            'email',
        ]
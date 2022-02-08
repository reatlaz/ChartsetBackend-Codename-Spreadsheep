from django.conf import settings
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Chartset

@registry.register_document
class ChartsetDocument(Document):
    class Index:
        name = 'chset'

    settings = {
        'number_of_shards': 1,
        'number_of replicas': 0
    }

    class Django:
        model = Chartset
        fields = [
            'name',
            'date_modified',
        ]
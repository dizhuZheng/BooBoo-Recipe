from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import UserProfile

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'users'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    class Django:
        model = UserProfile
        fields = [
            'username',
            'email',
            'address',
            'job',
            'gender',
            'date_joined',
        ]
        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000

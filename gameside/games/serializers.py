from shared.serializers import BaseSerializer


class GameSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'title': instance.title,
            'slug': instance.slug,
            'description': instance.description,
            'cover': self.build_url(instance.cover.url),
            'price': instance.price,
            'stock': instance.stock,
            'released_at': instance.released_at.isoformat(),
            'pegi': instance.pegi,
            'category': instance.category.name,
            'platforms': None,
        }

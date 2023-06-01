from rest_framework.serializers import ModelSerializer

from backend.models import Core, Boost


class CoreSerializer(ModelSerializer):
    class Meta:
        model = Core
        fields = ['coins', 'click_power']
class Boosterializer(ModelSerializer):
    class Meta:
        model = Boost
        fields = '__all__'

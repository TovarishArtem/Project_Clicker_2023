from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from backend.models import Core, Boost
from backend.serializers import CoreSerializer, Boosterializer


# Create your views here.
@api_view(['GET'])
def call_click(request):
    core = Core.objects.get(user=request.user)
    is_levelup = core.click()
    if is_levelup:
        Boost.objects.create(core=core, price=core.level * 50, power=core.level * 20)

    core.save()
    return Response({'core': CoreSerializer(core).data, 'is_levelup' : is_levelup})

class BoostViewSet(viewsets.ModelViewSet):
    queryset = Boost.objects.all()
    serializer_class = Boosterializer

    def get_queryset(self):
        core = Core.objects.get(user = self.request.user)
        boosts = Boost.objects.filter(core = core)
        return boosts
    def patrial_update(self, request, pk, **kwargs):
        boot = self.queryset.get(pk=pk)
        is_levelup = boost.levelup()
        if not is_levelup:
            return Response({'error': 'Не хватает денег'})
        old_boost_ststs, new_boost_stats = is_levelup
        return Response({
            'old_boost_ststs': self.serializer_class(old_boost_ststs).data,
            'new_boost_stats' : self.serializer_class(new_boost_stats).data
        })
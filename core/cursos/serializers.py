from rest_framework import serializers
from .models import *

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = '__all__'
        extra_kwargs = {
            'email': {'write_only': True}
        }
class CursoSerializer(serializers.ModelSerializer):
    #nested relationship
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #hyperlinked relationship
    #avaliacoes = serializers.HyperlinkedRelatedField(
    #    many=True,
    #    read_only=True,
    #    view_name='avaliacao-detail'
    #)

    #primary key relationship
    avaliacoes = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'url', 'criado_em', 'atualizado_em', 'ativo', 'avaliacoes']

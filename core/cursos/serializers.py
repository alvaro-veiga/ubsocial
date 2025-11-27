from rest_framework import serializers
from .models import *
from django.db.models import Avg

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = '__all__'
        extra_kwargs = {
            'email': {'write_only': True}
        }
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError('A avaliação deve estar entre 1 e 5.')



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

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ['id', 'titulo', 'url', 'criado_em', 'atualizado_em', 'ativo', 'avaliacoes', 'media_avaliacoes']

    def get_media_avaliacoes(self, obj):
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg')
        if media is None:
            return 0
        return round(media*2)/2

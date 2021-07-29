from rest_framework import serializers

class EnderecoCepSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'cep': instance['cep'],
            'localidade': instance['localidade'],
            'bairro': instance['bairro'],
            'logradouro': instance['logradouro'],
            'uf': instance['uf'],
            'complemento': instance['complemento'],
            'ibge': instance['ibge'],
        }
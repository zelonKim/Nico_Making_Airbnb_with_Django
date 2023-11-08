from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category # set the Model to be serialized
        fields = "__all__" # serializes all fields
          # fields = ("name", "kind",) # serializes only the specific fields 
          # exclude=("created_at",) # serializes all fields with excluding the specific fields


"""
 class CategorySerializer(serializers.Serializer):
     # serializers.변환될 타입 함수()
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    kind = serializers.ChoiceField(choices=Category.CatgoryKindChoices.choices)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data) # {'name': 'DRF', 'kind': 'rooms'}
        return Category.objects.create(**validated_data) # name='DRF', kind="rooms"
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name) # get('찾을 키', '찾는 키가 없을 경우의 기본값')
        instance.kind = validated_data.get('kind', instance.kind)
        instance.save()
        return instance 
"""
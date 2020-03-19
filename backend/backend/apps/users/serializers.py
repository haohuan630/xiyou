from rest_framework import serializers

from users.models import Area, PersonInfo


class AreaSerializer(serializers.ModelSerializer):
    """地区序列化器类"""
    class Meta:
        model = Area
        fields = ('id', 'name')


class SubAreaSerializer(serializers.ModelSerializer):
    """地区序列化器类"""
    # 使用指定的序列化器进行序列化
    subs = AreaSerializer(label='下级地区', many=True)

    class Meta:
        model = Area
        fields = ('id', 'name', 'subs')


class PersonSerializer(serializers.ModelSerializer):
    """人员信息序列化器类"""
    class Meta:
        model = PersonInfo
        fields = ('id', 'name', 'url', 'views', 'brief_intro')



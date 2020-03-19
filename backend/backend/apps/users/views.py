from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
# from rest_framework_extensions.cache.mixins import CacheResponseMixin

from users.models import Area, PersonInfo
from users.serializers import AreaSerializer, SubAreaSerializer, PersonSerializer


# Create your views here.

# 视图集: 将操作同一组资源的处理函数放在同一类中
class AreaViewSet(ReadOnlyModelViewSet):
    """地区的查询集"""
    # 关闭当前视图分页
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return AreaSerializer
        else:
            return SubAreaSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None)
        else:
            return Area.objects.all()


# GET /areas/
# class AreasView(GenericAPIView):
class AreasView(ListAPIView):
    # 指定当前视图所使用的序列化类
    serializer_class = AreaSerializer
    # 指定当前视图所使用的查询集
    queryset = Area.objects.filter(parent=None)

    # def get(self, request):
    #     """
    #     获取所有省级地区的信息:
    #     1. 查询所有省级地区的信息
    #     2. 将省级地区的信息序列化并返回
    #     """
    #     # 1. 查询所有省级地区的信息
    #     areas = self.get_queryset()
    #
    #     # 2. 将省级地区的信息序列化并返回
    #     serializer = self.get_serializer(areas, many=True)
    #     return Response(serializer.data)


# GET /areas/(?P<pk>\d+)/
# class SubAreasView(GenericAPIView):
class SubAreasView(RetrieveAPIView):
    serializer_class = SubAreaSerializer
    queryset = Area.objects.all()

    # def get(self, request, pk):
    #     """
    #     获取指定地区的信息:
    #     1. 根据pk获取指定的地区信息
    #     2. 将地区序列化并返回(注: 将地址关联的下级地区进行嵌套序列化)
    #     """
    #     # 1. 根据pk获取指定的地区信息
    #     area = self.get_object()
    #
    #     # 2. 将地区序列化并返回(注: 将地址关联的下级地区进行嵌套序列化)
    #     serializer = self.get_serializer(area)
    #     return Response(serializer.data)


class PersonInfoView(GenericAPIView):
    """人员信息查询"""
    serializer_class = PersonSerializer

    def get(self, request, pk):
        person_obj = Area.objects.get(id=pk)
        if person_obj:
            # print(person_obj.personinfo_set.values())
            person_data = person_obj.personinfo_set.values()
            # serializer = self.get_serializer(person_data)
        else:
            person_data = {}

        return Response(person_data)

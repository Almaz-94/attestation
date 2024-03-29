from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from retail.models import Member
from retail.serializers import MemberSerializer, MemberUpdateSerializer
from users.permissions import IsActive


class MemberCreateAPIView(CreateAPIView):
    """ Представление создания компании """
    serializer_class = MemberSerializer
    permission_classes = [IsActive, IsAuthenticated]

class MemberListAPIView(ListAPIView):
    """ Представление списка зарегистрированных компаний """
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('country',)
    permission_classes = [IsActive, IsAuthenticated]

class MemberUpdateAPIView(UpdateAPIView):
    """ Представление редактирования данных компании """
    serializer_class = MemberUpdateSerializer
    permission_classes = [IsActive, IsAuthenticated]
    queryset = Member.objects.all()

class MemberRetrieveAPIView(RetrieveAPIView):
    """ Представление просмотра профиля компании """
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    permission_classes = [IsActive, IsAuthenticated]

class MemberDestroyAPIView(DestroyAPIView):
    """ Представление удаления компании из сети  """
    queryset = Member.objects.all()
    permission_classes = [IsActive, IsAuthenticated]


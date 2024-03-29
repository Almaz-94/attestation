from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

from retail.models import Member
from retail.serializers import MemberSerializer, MemberUpdateSerializer
from users.permissions import IsActive


class MemberCreateAPIView(CreateAPIView):
    serializer_class = MemberSerializer
    permission_classes = [IsActive,]

class MemberListAPIView(ListAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    permission_classes = [IsActive, ]

class MemberUpdateAPIView(UpdateAPIView):
    serializer_class = MemberUpdateSerializer
    permission_classes = [IsActive, ]
    queryset = Member.objects.all()

class MemberRetrieveAPIView(RetrieveAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    permission_classes = [IsActive, ]

class MemberDestroyAPIView(DestroyAPIView):
    queryset = Member.objects.all()
    permission_classes = [IsActive, ]


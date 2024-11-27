from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import Group

# Create your views here.
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        groups = [group.name for group in user.groups.all()]
        return Response ({
            "username": user.username,
            "is_superuser": user.is_superuser,
            "groups": groups
        })


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticated]

class PaketViewSet(viewsets.ModelViewSet):
    queryset = Paket.objects.all()
    serializer_class = PaketSerializer
    permission_classes = [IsAuthenticated]

class TransaksiViewSet(viewsets.ModelViewSet):
    queryset = Transaksi.objects.all()
    serializer_class = TransaksiSerializer
    permission_classes = [IsAuthenticated]
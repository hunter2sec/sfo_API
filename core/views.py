# -*- coding: utf-8 -*-

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, BasePermission, SAFE_METHODS

from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import viewsets
from .serializers import UserSerializer, ItemSerializer

from .models import Item

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method == 'GET'

class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        is_authenticated = IsAuthenticated.has_permission(self, request, view)
        return is_authenticated and request.method in SAFE_METHODS or is_admin

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed and edited by admins.
    """
    permission_classes = {IsAdminUser}
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed
    """
    permission_classes = {IsAdminUserOrReadOnly}
    # permission_classes = {IsAdminUser|IsAuthenticated&ReadOnly}
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
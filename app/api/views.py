from app.models import UserRegisterModel
from rest_framework import viewsets
from app.api.serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserRegisterModel.objects.all()
    serializer_class = UserSerializer
    authentication_classess = [SessionAuthentication]
    permission_classess = [IsAuthenticatedOrReadOnly]
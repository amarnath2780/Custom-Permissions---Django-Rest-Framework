from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from rest_framework.viewsets  import ModelViewSet 
from rest_framework.views import APIView
from .models import Post, Category
from .serializers import PostSerializer , CategorySerializer
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


class CategroryAddViewSet(APIView):

    def post(self, request:Response):
        
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Message' : 'Categroy created succesfuly'} , status=status.HTTP_200_OK)
        else:
            return Response({"Message" : 'Invalid data'} , status=status.HTTP_400_BAD_REQUEST)


class PostAddViewSet(APIView):

    def post(self, request:Response):

        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Message' : 'A post uploaded'} , status=status.HTTP_200_OK)
        else:
            return Response({'Message' : 'Invalid Data'}, status=status.HTTP_400_BAD_REQUEST)
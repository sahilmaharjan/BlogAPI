from rest_framework.views import APIView
from .serializers import CreateBlogSerializer, BlogSerializer, UpdateBlogSerializer
from rest_framework.response import Response
from rest_framework import status  
from rest_framework.permissions import IsAuthenticated
from .models import Post
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly, IsOwner
from .paginations import BlogListPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class CreateBlog(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request, format = None):
        print(request.user.id, "request user")
        serializer = CreateBlogSerializer(data = request.data, context = {'user': request.user})
        # serializer = CreateBlogSerializer(data = request.data)

        if serializer.is_valid():
             blog = serializer.save()
             print(blog, "blogggggggggggggggggggg")
            #  print(blog.author, "author name")
             return Response({
                'msg' : 'Blog Posted'
            }, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteBlog(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def delete(self, request, pk, format=None):
        try:
            blog = Post.objects.get(id=pk)
            print('blog================>', blog)
            self.check_object_permissions(request, blog.author)
            blog.delete()
            return Response({'msg': 'Blog deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response({'error': 'Blog not found.'}, status=status.HTTP_404_NOT_FOUND)

class BlogList(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = BlogListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    def get(self, request,pk = None, format=None):
        if pk:
            print(pk)
            blog = Post.objects.get(id=pk)
            serializer = BlogSerializer(blog)

        else:
            blogs = Post.objects.all()
            serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateBlog(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def patch(self, request, pk, format=None):
        blog = Post.objects.get(id = pk)
        # message = "You do not have permisssions to edit this blog"
        self.check_object_permissions(request, blog.author.id) # explicitly called
        serializer = UpdateBlogSerializer(blog, data=request.data, context = {'user': request.user})
        print(serializer,"---------------------------------------")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
                'msg': 'You are not the owner of this blog.',
                'errors': serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)

class MyBlog(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def get(self, request):
        print("user ---------->",request.user.id)
        blogs = Post.objects.filter(author = request.user.id)
        print(blogs,"my blogs only-------------------------")
        for b in blogs:
            print(b,"----------")
        serializer = BlogSerializer(blogs, many=True)
        print(serializer,"my serializer-------------------------")
        return Response(serializer.data, status=status.HTTP_200_OK)

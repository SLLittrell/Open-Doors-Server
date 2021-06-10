from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from open_doors_api.models import Post, Category, OpenUser


class PostView(ViewSet):

    def create(self, request):
        """Handle POST operations
        Returns:
            Response -- JSON serialized post instance
        """

        user = OpenUser.objects.get(user=request.auth.user)
        category = Category.objects.get(pk=request.data["category_id"])

        post = Post()
        post.title = request.data['title']
        post.category = category
        post.publication_date = request.data['publication_date']
        post.image_url = request.data['image_url']
        post.social_story = request.data['social_story']
        post.visual_schedule = request.data['visual_schedule']
        post.content = request.data['content']
        post.approved = request.data['approved']
        post.user = user
    

      
        try:
            post.save()
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        """Handle GET requests for single post
        Returns:
            Response -- JSON serialized game instance
        """
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)
        
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code
        """
        user = OpenUser.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=pk)
        post.title = request.data['title']
        post.publication_date = request.data['publication_date']
        post.image_url = request.data['image_url']
        post.content = request.data['content']
        post.user = user

        category = Category.objects.get(pk=request.data["category_id"])
        post.category = category
        post.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single post
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            post = Post.objects.get(pk=pk)
            post.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        post = Post.objects.all()

        
        category = self.request.query_params.get('category', None)
        if category is not None:
            posts = post.filter(category__id=category)

        serializer = PostSerializer(
            post, many=True, context={'request': request})
        return Response(serializer.data)


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']

class PostOpenUserSerializer(serializers.ModelSerializer):

    user = PostUserSerializer(many=False)
    class Meta:
        model = OpenUser
        fields = ['user']


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    Arguments:
        serializer type
    """
    user = PostUserSerializer(many=False)
    class Meta:
        model = Post
        fields = ('id', 'title', 'publication_date', 'image_url', 'content', 'category', 'user', 'social_story_id', 'visual_schedule_id')
        depth = 1
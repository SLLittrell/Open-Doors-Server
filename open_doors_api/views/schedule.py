from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import action
import datetime
from open_doors_api.models import VisualSchedule, OpenUser


class VisualScheduleView(ViewSet):
    def create(self, request):
        """Ensure client can create a story"""
        schedule =VisualSchedule()
        user = user = OpenUser.objects.get(user=request.auth.user)
        schedule.user =user.user
        schedule.title = (request.data['title'])
        schedule.activity_1 = (request.data['activity_1'])
        schedule.image_1 = (request.data['image_1'])
        schedule.activity_2 = (request.data['activity_2'])
        schedule.image_2 = (request.data['image_2'])
        schedule.activity_3 = (request.data['activity_3'])
        schedule.image_3 = (request.data['image_3'])
        schedule.activity_4 = (request.data['activity_4'])
        schedule.image_4 = (request.data['image_4'])
        schedule.activity_5 = (request.data['activity_5'])
        schedule.image_5 = (request.data['image_5'])
        schedule.activity_6 = (request.data['activity_6'])
        schedule.image_6 = (request.data['image_6'])
        schedule.activity_7 = (request.data['activity_7'])
        schedule.image_7 = (request.data['image_7'])
        schedule.activity_8 = (request.data['activity_8'])
        schedule.image_8 = (request.data['image_8'])
        schedule.activity_9 = (request.data['activity_9'])
        schedule.image_9 = (request.data['image_9'])
        schedule.activity_10 = (request.data['activity_10'])
        schedule.image_10 = (request.data['image_10'])

        try:
            schedule.save()
            serializer = ScheduleSerializer(schedule, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self,request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        schedule = VisualSchedule.objects.all()
        serializer = ScheduleSerializer(
            schedule, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self,request, pk=None):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        try:
            schedule = VisualSchedule.objects.get(pk=pk)
            serializer = ScheduleSerializer(
                schedule, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def update(self, request, pk=None):
        """Handle PUT requests for a schedule
        Returns:
            Response -- Empty body with 204 status code
        """
        schedule =VisualSchedule.objects.get(pk=pk)
        user = OpenUser.objects.get(user=request.auth.user)
        schedule.user =user.user
        schedule.title = (request.data['title'])
        schedule.activity_1 = (request.data['activity_1'])
        schedule.image_1 = (request.data['image_1'])
        schedule.activity_2 = (request.data['activity_2'])
        schedule.image_2 = (request.data['image_2'])
        schedule.activity_3 = (request.data['activity_3'])
        schedule.image_3 = (request.data['image_3'])
        schedule.activity_4 = (request.data['activity_4'])
        schedule.image_4 = (request.data['image_4'])
        schedule.activity_5 = (request.data['activity_5'])
        schedule.image_5 = (request.data['image_5'])
        schedule.activity_6 = (request.data['activity_6'])
        schedule.image_6 = (request.data['image_6'])
        schedule.activity_7 = (request.data['activity_7'])
        schedule.image_7 = (request.data['image_7'])
        schedule.activity_8 = (request.data['activity_8'])
        schedule.image_8 = (request.data['image_8'])
        schedule.activity_9 = (request.data['activity_9'])
        schedule.image_9 = (request.data['image_9'])
        schedule.activity_10 = (request.data['activity_10'])
        schedule.image_10 = (request.data['image_10'])

        # Try/Except try to save new post instance and use serializer to convert to json
        try:
            schedule.save()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single schedule
        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            schedule = VisualSchedule.objects.get(pk=pk)
            schedule.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except VisualSchedule.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ScheduleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username']


class ScheduleOpenUserSerializer(serializers.ModelSerializer):

    user = ScheduleUserSerializer(many=False)
    class Meta:
        model = OpenUser
        fields = ['user']

class ScheduleSerializer(serializers.ModelSerializer):

    user = ScheduleUserSerializer(many=False)
    class Meta:
        model = VisualSchedule
        fields = ['id','user','publication_date', 'title',
                            'activity_1',
                            'image_1' ,
                            'activity_2', 
                            'image_2' ,
                            'activity_3', 
                            'image_3', 
                            'activity_4', 
                            'image_4', 
                            'activity_5', 
                            'image_5', 
                            'activity_6', 
                            'image_6', 
                            'activity_7', 
                            'image_7', 
                            'activity_8', 
                            'image_8', 
                            'activity_9', 
                            'image_9', 
                            'activity_10', 
                            'image_10']
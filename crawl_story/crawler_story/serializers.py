from .models import Story, Chaper, Category
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ['categorys']


class ChaperSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Chaper
		fields = ['name_story', 'name_chap', 'content', 'status', 'create_date']


class StorySerializer(serializers.HyperlinkedModelSerializer):
	categorys = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Category')
	chaper = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='Chaper')

	class Meta:
		model = Story
		fields = ['id', 'name_story', 'categorys', 'image', 'status', 'author', 'content_story', 'date_refresh', 'chaper']

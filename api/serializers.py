from rest_framework import serializers
from .models import Question, Category, Upvote, Downvote
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField(style={'input_type':'password'}, write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)

	def validate(self, data):
		my_username = data.get('username')
		my_password = data.get('password')

		if my_username == '':
			raise serializers.ValidationError("A username is required to login.")

		try:
			user_obj = User.objects.get(username=my_username)
		except:
			raise serializers.ValidationError("This username does not exist")

		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination! Noob..")


		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)

		data["token"] = token
		return data


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']




class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_content', 'user', 'timestamp', 'image']


class UpvoteCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Upvote
		fields = ['question']

class UpvoteListSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Upvote
		fields = ['question']

class DownvoteCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Downvote
		fields = ['question']

class DownvoteListSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Downvote
		fields = ['question']


class QuestionDetailSerializer(serializers.ModelSerializer):
    upvotes = serializers.SerializerMethodField()
    downvotes = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['question_content', 'user', 'timestamp', 'image' 'upvotes', 'downvotes']

        def get_upvotes(self, obj):
            # likes = Like.objects.filter(article=obj)
            upvotes = obj.upvote_set.all()
            json_upvotes = UpvoteListSerializer(upvotes, many=True).data
            return json_upvotes

        def get_downvotes(self, obj):
            # likes = Like.objects.filter(article=obj)
            downvotes = obj.downvote_set.all()
            json_downvotes = DownvoteListSerializer(downvotes, many=True).data
            return json_downvotes


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_title', 'user', 'timestamp', 'category_description', 'image']


class DownvoteListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Downvote
        fields = ['question']

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_title', 'user', 'timestamp', 'category_description', 'image']

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        def create(self, validated_data):
            new_user = User(**validated_data)
            new_user.set_password(validated_data['password'])
            new_user.save()
            return validated_data
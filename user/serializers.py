# from rest_framework import serializers
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 
#                  'bonus_card_number', 'bonus_points', 'phone_number']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
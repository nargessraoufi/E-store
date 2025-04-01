# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     bonus_card_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
#     bonus_points = models.PositiveIntegerField(default=0)
#     phone_number = models.CharField(max_length=20, blank=True)
    
#     # حل مشکل related_name
#     groups = models.ManyToManyField(
#         'auth.Group',
#         verbose_name='groups',
#         blank=True,
#         help_text='The groups this user belongs to.',
#         related_name="customuser_set",
#         related_query_name="user",
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         verbose_name='user permissions',
#         blank=True,
#         help_text='Specific permissions for this user.',
#         related_name="customuser_set",
#         related_query_name="user",
#     )
    
#     def __str__(self):
#         return self.username
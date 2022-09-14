from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
# Create your models here.

# class User(AbstractBaseUser):
#     name = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth']

#     def __str__(self):
#         return self.name

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

class Category(models.Mode):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')


class Like(models.Model):
    is_active = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes"
    )



class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    user = models.ManyToManyField(User)

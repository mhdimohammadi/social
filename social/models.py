from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from taggit.managers import TaggableManager
from django_resized import ResizedImageField


class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='account/images')
    job = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=11)
    following = models.ManyToManyField('self', through='Contact', related_name="follower", symmetrical=False)

    def get_absolute_url(self):
        return reverse("social:user_detail", args=[self.username])


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    saved_by = models.ManyToManyField(User, related_name="saved_posts")
    tags = TaggableManager()
    total_likes = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.author)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
            models.Index(fields=['-total_likes'])
        ]

    def get_absolute_url(self):
        return reverse("social:post_detail", args=[self.id])


class Contact(models.Model):
    user_from = models.ForeignKey(User, related_name="rel_from_set", on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name="rel_to_set", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['-created'])]
        ordering = ['-created']

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image_file = ResizedImageField(upload_to='post_images/', size=[500, 500], quality=75, crop=['middle', 'center'],
                                   null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

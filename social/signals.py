from django.core.mail import send_mail
from django.db.models.signals import m2m_changed, post_delete, post_init
from django.dispatch import receiver
from .models import Post, User


@receiver(m2m_changed, sender=Post.likes.through)
def user_like_change(sender, instance, **kwargs):
    instance.total_likes = instance.likes.count()
    instance.save()


@receiver(post_delete, sender=Post)
def post_delete_email(sender, instance, **kwargs):
    author = instance.author
    subject = "your post has been deleted!"
    message = f"your post has been deleted(id:{instance.id})"
    send_mail(subject, message, 'kingnima949@gmail.com', [author.email], fail_silently=False)


@receiver(post_init, sender=User)
def fill_account(sender, instance, **kwargs):
    instance.date_of_birth = "2000-1-1"
    instance.bio = "No bio available"
    instance.job = "No job available"


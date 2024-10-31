from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.core.mail import send_mail


def make_deactivated(modeladmin, request, queryset):
    results = queryset.update(active=False)
    modeladmin.message_user(request, f"{results} post were deactivated")


make_deactivated.short_description = "deactivate"


def make_activate(modeladmin, request, queryset):
    results = queryset.update(active=True)
    modeladmin.message_user(request, f"{results} post were activated")


make_activate.short_description = "activate"


def email_status(modeladmin, request, queryset):
    subject = "post status"
    for post in queryset:
        if post.author.email:
            message = f"your post status is {post.active}"
            send_mail(subject, message, "kingnima949@gmail.com", [post.author.email])
            modeladmin.message_user(request, "email has been sent.")
        else:
            modeladmin.message_user(request, f"{post.author} doesnt have email")


email_status.short_description = "email status"


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['username', 'phone', 'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {"fields": ('date_of_birth', 'bio', 'photo', 'job', 'phone')}),
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'description', 'active']
    ordering = ['created']
    search_fields = ['description']
    actions = [make_deactivated, make_activate, email_status]


admin.site.register(Contact)

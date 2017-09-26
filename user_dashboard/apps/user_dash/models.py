# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    USER_TYPES = (
        (1, 'Normal'),
        (9, 'Admin'),
    )
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)
    user_level = models.IntegerField(choices=USER_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages")
    for_user = models.ForeignKey(User, related_name="wall_msgs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    msg = models.ForeignKey(Message, related_name="comments")
    user = models.ForeignKey(User, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

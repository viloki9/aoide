from django.db import models
from json_field import JSONField
from django_extensions.db.fields import UUIDField

class SynBase(models.Model):
    name = models.CharField(max_length=255)
    meta = JSONField(null=True, blank=True)

class SynWord(models.Model):
    name = models.CharField(max_length=255)
    synonym_root = models.ForeignKey(SynBase, null=True)
    meta = JSONField(null=True, blank=True)


##Tree Node Models##

class TreeNode(models.Model):
    guid = UUIDField()
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    disambiguation = models.CharField(null=True, blank=True, max_length=255)
    src_id = models.CharField(null=True, blank=True, max_length=255)
    src_url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    meta = JSONField(null=True, blank=True)

    class Meta:
        unique_together = ('name', 'disambiguation')

class Genre(models.Model):
    name = models.CharField(max_length=255)
    node = models.ForeignKey(TreeNode, related_name='genre')
    meta = JSONField(null=True, blank=True)

class TreeEdge(models.Model):
    guid = UUIDField()
    parent = models.ForeignKey(TreeNode, null=True, related_name='parent')
    child = models.ForeignKey(TreeNode, null=True, related_name='child')
    created = models.DateTimeField(auto_now_add=True)
    meta = JSONField(null=True, blank=True)


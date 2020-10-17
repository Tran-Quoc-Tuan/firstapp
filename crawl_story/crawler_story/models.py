from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    categorys = models.CharField(max_length=15, unique=True, blank=True, null=True)

    def __str__(self):
        return self.categorys


class Story(models.Model):
    name_story = models.CharField(max_length=50, blank=True, null=True)
    categorys = models.ManyToManyField(Category)
    image = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    author = models.CharField(max_length=30, blank=True, null=True)
    content_story = models.TextField(blank=True, null=True)
    date_refresh = models.DateTimeField()

    def __str__(self):
        return self.name_story


class Chaper(models.Model):
    name_story = models.ForeignKey(Story, related_name='chaper', on_delete=models.CASCADE, blank=True, null=True)
    name_chap = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    create_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name_chap

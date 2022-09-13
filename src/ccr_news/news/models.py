from django.db import models


class NewsTypes(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    colour = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    full_description = models.TextField()
    new_type = models.ForeignKey(NewsTypes, on_delete=models.PROTECT, related_name="get_news")

    def __str__(self):
        return self.title

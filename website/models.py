from statistics import mode
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Hyperlink(models.Model):
    registration_google_form = models.TextField()
    group_invite_link = models.TextField()

class Blog(models.Model):
    title = models.TextField()
    link = models.TextField()
    blog_image = models.ImageField(upload_to= 'blog_image')
    slug = models.SlugField(max_length=264, unique=True, editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Blog, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title) + "-" + str(self.id)
            self.save()

class Event(models.Model):
    title = models.TextField()
    event_name = models.ImageField(upload_to= 'event_name')
    event_poster = models.ImageField(upload_to= 'event_poster')
    link = models.TextField()
    slug = models.SlugField(max_length=264, unique=True, editable=False, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title) + "-" + str(self.id)
            self.save()
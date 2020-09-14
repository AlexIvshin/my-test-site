from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    class Meta:
        ordering = ['-date_pub']

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)


class Script(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True)
    body = models.TextField()
    description = models.CharField(max_length=150,blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='scripts')

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('script_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('script_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_delete_url(self):
        return reverse('script_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Link(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50,blank=True, unique=True)
    description = models.CharField(max_length=150,blank=True, db_index=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Man(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50,blank=True, unique=True)
    body = models.TextField()


    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('man_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('man_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_delete_url(self):
        return reverse('man_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Command(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,blank=True, unique=True)
    body = models.TextField()

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('command_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('command_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def get_delete_url(self):
        return reverse('command_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

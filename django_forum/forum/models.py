from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import math
# Create your models here.

class Section(models.Model):
    """
    name_section = name of discussion
    created by admins
    """
    name_section = models.CharField(max_length=80)
    description = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name_section
    def get_absolute_url(self):
        return reverse("view_section", kwargs={"pk": self.pk})
    
    def get_last_discussions(self):
        return Discussion.objects.filter(section_membership = self).order_by("-data_creation")[:2]

    def get_number_of_posts_in_section(self):
        return Post.objects.filter(discussion__section_membership=self).count()
    

class Discussion(models.Model):
    title = models.CharField(max_length=120)
    data_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="discussions")
    section_membership = models.ForeignKey(Section, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("view_discussion", kwargs={"pk": self.pk})

    def get_n_pages(self):
        posts_discussion = self.post_set.count()
        n_pages = math.ceil(posts_discussion / 5)
        return n_pages


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Discussion"
        verbose_name_plural = "Discussions"

class Post(models.Model):
    author_post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    data_creation = models.DateTimeField(auto_now_add=True)
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.author_post.username
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Post"

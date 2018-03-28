from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    """ User Model """

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified')
    )

    CATEGORY_CHOICES = (
        ('VIDEO & FLIM', 'VIDEO & FLIM'),
        ('MUSIC', 'MUSIC'),
        ('WRITING', 'WRITING'),
        ('COMICS & ILLUSTRATION', 'COMICS & ILLUSTRATION'),
        ('PODCASTS', 'PODCASTS'),
        ('GAMES', 'GAMES'),
        ('DRAWING & PAINTING', 'DRAWING & PAINTING'),
        ('ANIMATION', 'ANIMATION'),
        ('PHOTOGRAPHY', 'PHOTOGRAPHY'),
        ('SCIENCE','SCIENCE'),
        ('EDUCATION','EDUCATION'),
        ('CRAFT & DIY','CRAFT & DIY'),
        ('DANCE & THEATER', 'DANCE & THEATER'),
        ('EVERYTHING ELSE','EVERYTHING ELSE'),


    )
    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    website = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True, blank=True)
    followers = models.ManyToManyField("self", blank=True)
    following = models.ManyToManyField("self", blank=True)
    category = models.CharField(max_length=80, choices=CATEGORY_CHOICES, null=True)
    donation = models.BigIntegerField(default=0, blank=True)
    def __str__(self):
        return self.username

    @property
    def post_count(self):
        return self.buckets.all().count()

    @property
    def followers_count(self):
        return self.followers.all().count()

    @property
    def following_count(self):
        return self.following.all().count()

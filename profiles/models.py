from django.db import models
from model_utils.models import TimeStampedModel


class Profile(TimestampedModel):
    user = models.OneToOneField(
        'customauth.User', on_delete=models.CASCADE
    )

    theme = models.TextField(blank=True) # make this a choice

    follows = models.ManyToManyField(
        'self',
        related_name='followed_by',
        symmetrical=False
    )

    favorites = models.ManyToManyField(
        'articles.Article',
        related_name='favorited_by'
    )


    def __str__(self):
        return self.user.username

    def follow(self, profile):
        """Follow `profile` if we're not already following `profile`."""
        self.follows.add(profile)

    def unfollow(self, profile):
        """Unfollow `profile` if we're already following `profile`."""
        self.follows.remove(profile)

    def is_following(self, profile):
        """Returns True if we're following `profile`; False otherwise."""
        return self.follows.filter(pk=profile.pk).exists()

    def is_followed_by(self, profile):
        """Returns True if `profile` is following us; False otherwise."""
        return self.followed_by.filter(pk=profile.pk).exists()

    def favorite(self, article):
        """Favorite `article` if we haven't already favorited it."""
        self.favorites.add(article)

    def unfavorite(self, article):
        """Unfavorite `article` if we've already favorited it."""
        self.favorites.remove(article)

    def has_favorited(self, article):
        """Returns True if we have favorited `article`; else False."""
        return self.favorites.filter(pk=article.pk).exists()

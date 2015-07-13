# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible
class TopicFavorite(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    topic = models.ForeignKey('spirit.Topic')

    date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'topic')
        ordering = ['-date', '-pk']
        verbose_name = _("favorite")
        verbose_name_plural = _("favorites")
        db_table = 'spirit_favorite_topicfavorite'  # TODO: remove in Spirit 0.4

    def __str__(self):
        return "%s bookmarked %s" % (self.user, self.topic)

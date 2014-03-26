from django.utils.translation import ugettext as _
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    publish_date = models.DateTimeField()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __unicode__(self):
        return u'%s' % self.title


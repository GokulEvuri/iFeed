from django.db import models

class Website(models.Model):
    web_url = models.URLField(max_length=254)

    def __unicode__(self):
        return unicode(self.web_url)

from django.db import models
from django.shortcuts import reverse

class StorageVK(models.Model):
    slug = models.SlugField(unique=True)
    post_query = models.TextField()
    post_type = models.TextField()
    post_ownert = models.TextField()
    post_date = models.DateTimeField()
    post_link = models.TextField(primary_key=True)
    post_id = models.TextField()
    post_owner = models.TextField()
    post_text = models.TextField()
    post_score = models.TextField()
    post_keyword = models.TextField()
    post_mark = models.TextField()
    post_len = models.TextField()
    post_category = models.TextField()
    post_textp = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = str(self.post_owner) + str(self.post_id)
        super(StorageVK, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={"slug": self.slug})

    def __str__(self):
        return self.post_link



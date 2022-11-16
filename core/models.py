from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
  title = models.CharField('Titulo', max_length=200, blank=False, null=False,default='')
  subtitle = models.CharField('Subtitulo', max_length=500, blank=False, null=False,default='')
  content = models.TextFielcontent = RichTextField()
  date = models.DateField('Data de Publicação', auto_now_add=True)
  slug = models.SlugField('Slug', editable=False,default='')

  def __str__(self):
    return self.title

  # def save(self, *args, **kwargs):
  #   value = self.title
  #   self.slug = slugify(value, allow_unicode= True)
  #   super().save(*args, **kwargs)

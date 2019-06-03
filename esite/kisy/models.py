from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList, InlinePanel, StreamFieldPanel, MultiFieldPanel, FieldPanel
from wagtail.images.blocks import ImageChooserBlock


class Customer(AbstractUser):
  customerID = models.AutoField(primary_key=True)
  email = models.EmailField(null=True, blank=False)
  title = models.BooleanField(null=True, blank=False)
  firstName = models.CharField(null=True, blank=False, max_length=20)
  lastName = models.CharField(null=True, blank=False, max_length=20)
  password = models.CharField(null=True, blank=False, max_length=512)
  
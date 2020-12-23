
from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class WorkerCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Category (admin work)"

@receiver(pre_save,sender=WorkerCategory)
def pre_save_category_slug(sender,instance,**kwargs):
    instance.slug=slugify(instance.name)


class WorkingArea(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = " Area (admin work)"

@receiver(pre_save,sender=WorkingArea)
def pre_save_area_slug(sender,instance,**kwargs):
    instance.slug=slugify(instance.name)


# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super(PublishedManager, self).get_queryset().filter(status=True)
#
# class AllObjectManager(models.Manager):
#     def get_queryset(self):
#         return super(AllObjectManager, self).get_queryset()

class WorkerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='worker_profile')
    fullname = models.CharField(max_length=40,null=True,blank=True)
    category = models.ForeignKey(WorkerCategory,on_delete=models.CASCADE,null=True,blank=True)
    working_time = models.CharField(max_length=100,null=True,blank=True)
    hourly_rate  = models.FloatField(null=True,blank=True)
    working_area = models.ManyToManyField(WorkingArea)
    extra_service = models.CharField(max_length=250,null=True,blank=True)
    experience = models.FloatField(null=True,blank=True)
    phone      = models.IntegerField(null=True,blank=True)
    views      = models.PositiveIntegerField(default=0, blank=True)
    image      = models.ImageField(upload_to='profile_pic/',blank=False,null=False,default="default.jpg")

    created    = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=False)

    # published = PublishedManager()
    # objects   = AllObjectManager()


    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-views']


        verbose_name_plural = "Worker Profiles"


@receiver(pre_save, sender=WorkerProfile)
def check_status_of_profile(instance, *args, **kwargs):
    if (instance.fullname is not None and instance.category is not None and instance.working_time is not None
        and instance.hourly_rate is not None and instance.phone is not None):
        instance.status = True
    else:
        instance.status = False

class Message(models.Model):
    worker = models.ForeignKey(WorkerProfile,on_delete=models.CASCADE,related_name='worker_message')
    name  = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(blank=True,null=True)
    phone = models.IntegerField()
    message=models.TextField(blank=False,null=False)
    time =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-time']
        verbose_name_plural="Messages"


# when user create also create a profile
@receiver(post_save,sender=User)
def post_create_profile(instance,created,*args,**kwargs):
    if created:
        WorkerProfile.objects.get_or_create(user=instance)




from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Products(models.Model):
    title = models.CharField(max_length=25, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"




class Lessons(models.Model):
    title = models.CharField(max_length=500, db_index=True, verbose_name="Название")
    link = models.CharField(max_length=500, verbose_name="Ссылка на видео")
    duration = models.IntegerField(verbose_name="Длительность просмотра")
    products = models.ManyToManyField("Products", verbose_name="Продукт")
    file = models.FileField(blank=True,null=True)

    def get_products(self):
        return ",".join([str(p) for p in self.products.all()])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField("Products", related_name="products", verbose_name="Продукт")

    def get_products(self):
        return ",".join([str(p) for p in self.products.all()])

    class Meta:
        verbose_name = "Доступ"
        verbose_name_plural = "Доступы"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



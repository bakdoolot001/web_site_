from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    email = models.EmailField()
    phone1 = models.CharField(max_length=250)
    phone2 = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)
    image = models.ImageField(upload_to="image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

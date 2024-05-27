from django.db import models

# Create your models here.

class CategorySings(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'category_signs'

    def __str__(self):
        return f"{self.name}"

class RoadSingns(models.Model):
    categoriy = models.ForeignKey(CategorySings, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.FileField(upload_to='videos', blank=True, null=True)
    audio = models.FileField(upload_to='audio', blank=True, null=True)
    dock = models.FileField(upload_to='dock', blank=True, null=True)


    class Meta:
        db_table = 'road_signs'

    def __str__(self):
        return f"{self.categoriy.name}| {self.name}"
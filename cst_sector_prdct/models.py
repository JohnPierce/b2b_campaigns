from django.db import models

# Create your models here.


class Sector(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Industry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sector.name} -> {self.name}'

class VerticalMarket(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.industry.name} -> {self.name}'

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    vertical_market = models.ForeignKey(VerticalMarket, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.vertical_market.name} -> {self.name}'

class Algorithm(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.application.name} -> {self.name}'
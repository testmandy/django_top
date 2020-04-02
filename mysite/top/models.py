from django.db import models

# Create your models here.


class Version(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Owner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bug(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    task = models.ForeignKey('Task', on_delete=models.CASCADE, default=None)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=None)
    state = models.ForeignKey('State', on_delete=models.CASCADE, default=None)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, default=None)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    name = models.CharField(max_length=70)
    success_cases = models.IntegerField(default=None)
    failed_cases = models.IntegerField(default=None)
    version = models.ForeignKey('Version', on_delete=models.CASCADE, default=None)
    create_time = models.DateTimeField(auto_now=True)
    operator = models.ForeignKey('Owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

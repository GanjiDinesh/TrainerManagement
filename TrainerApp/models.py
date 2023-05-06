from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name

class Trainer(models.Model):
    trainer_name = models.CharField(max_length=50)
    phoneno = models.BigIntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class BatchAssign(models.Model):
    trainer_id = models.ForeignKey(Trainer,on_delete=models.CASCADE)
    batch_no = models.IntegerField()
    classroom = models.CharField(max_length=30)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    date_time = models.DateTimeField()




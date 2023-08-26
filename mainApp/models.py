from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Person'

class Passport(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.passport_number
    class Meta:
        unique_together = ['person', 'passport_number']
        db_table = 'Passport'

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Author'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Book'
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Student'

class CourseInfo(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'CourseInfo'

class Country(models.Model):
    name = models.CharField(max_length=250)
    becameIndependent = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Country'

class City(models.Model):
    name = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.IntegerField()
    continent = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'City'
    

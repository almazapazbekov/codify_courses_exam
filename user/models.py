import datetime
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=30)
    month_to_learn = models.IntegerField()

    def __str__(self):
        return self.name, self.month_to_learn

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.name == 'java script':
            self.name = 'Java Script'
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     # if AbstractPerson.phone_number.filter()
    #     #     pass
    #     # доделать
    #     self.phone_number =  .save()
    #     super().save(*args, **kwargs)


class Students(AbstractPerson):
    work_study_place = models.CharField(max_length=30, null=True)
    haw_own_notebook = models.BooleanField()
    os_choices = [
        (1, 'windows'),
        (2, 'macos'),
        (3, 'linux')
    ]
    preferred_os = models.CharField(max_length=30, choices=os_choices)


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=30, null=True)
    experience = models.DateField()
    mentor_relation = models.ManyToManyField(Students, through='Course')


class Course(models.Model):
    name = models.CharField(max_length=30)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    students = models.ForeignKey(Students, on_delete=models.CASCADE)

    def get_end_date(self):
        end_date = self.date_started.date() + datetime.timedelta(self.language.month_to_learn)
        return end_date

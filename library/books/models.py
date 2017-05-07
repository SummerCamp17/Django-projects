from django.db import models


class Book(models.Model):

    LOAN_STATUS = (
        (1, 'Available'),
        (0, 'Issued'),
    )

    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=LOAN_STATUS)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Author(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + str(" ") + self.last_name

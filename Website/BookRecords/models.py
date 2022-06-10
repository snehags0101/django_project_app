from django.db import models

class Allbooks(models.Model):
    bookname=models.CharField(max_length=500)
    authorname=models.CharField(max_length=500)
    def __str__(self):
        return self.bookname

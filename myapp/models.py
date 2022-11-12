from django.db import models


class Publisher(models.Model):
    pub_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null=True)
    price = models.CharField(max_length=10, null=True)
    available = models.CharField(max_length=20, null=True)
    publisher = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.book_id} - {self.title}"


class Member(models.Model):
    memb_id = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=50, null=True)
    memb_type = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200, null=True)
    memb_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.memb_id} - {self.name}"


class Brrowe_by(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    due_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add=True)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member} - {self.book}"



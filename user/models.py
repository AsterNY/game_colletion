from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField(upload_to='avatars/')
    contact_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    nickname = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='+')
    last_update_time = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='+')
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'user'

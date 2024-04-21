from django.db import models

class Display(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    ssh_public_key_or_password = models.TextField()
    remote_directory = models.CharField(max_length=255)

    def __str__(self):
        return self.name

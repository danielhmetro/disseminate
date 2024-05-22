from django.db import models
from django.conf import settings
import subprocess
import os
import sys

class Display(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    ssh_public_key_or_password = models.TextField()
    remote_directory = models.CharField(max_length=255)
    assigned_files = models.ManyToManyField('File', related_name='assigned_displays', blank=True)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='.')
    displays = models.ManyToManyField('Display', related_name='files', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        for display in Display.objects.all():
            self.sync_media(display)
            self.restart_viewer(display)

    def delete(self, *args, **kwargs):
        try:
            os.remove(self.file.path)
        except:
            pass
        for display in Display.objects.all():
            self.sync_media(display)
            self.restart_viewer(display)
        super().delete(*args, **kwargs)

    def sync_media(self, display):
        command = f"sshpass -p meshmesh9 rsync -e 'ssh -o StrictHostKeyChecking=no' -avu --delete {settings.MEDIA_ROOT} {display.username}@{display.ip_address}:{display.remote_directory}/"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Check if the command was successful
        if result.returncode == 0:
            print("Sync completed for {display.name} successfully.", file=sys.stdout)
            #print(result.stdout, file=sys.stdout)
        else:
            print("Sync failed for {display.name}. Error message:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)

    def restart_viewer(self, display):
        command = f"sshpass -p meshmesh9 ssh -o StrictHostKeyChecking=no {display.username}@{display.ip_address} 'sudo killall fbi; sudo fbi --noverbose -T 1 -a -t 5 {display.remote_directory}/media/*'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Check if the command was successful
        if result.returncode == 0:
            print("Viewer started on {display.name} successfully.", file=sys.stdout)
            #print(result.stdout, file=sys.stdout)
        else:
            print("Viewer start failed for {display.name}. Error message:", file=sys.stderr)
            print(result.stderr, file=sys.stderr)

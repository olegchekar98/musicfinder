from django.db import models
import datetime

class MusicianData(models.Model):
    #upload from social network
    name = models.CharField(max_length=50)
    photo = models.ImageField('''get in social network''')


class AudioExample(models.Model):
    name = models.CharField(max_length=50)
    audio_file = models.AudioField(upload_to='upload/audiofiles', blank=True,
                            ext_whitelist=('.mp3', '.wav', '.ogg'),
                            verbose_name=_('audio file'))

class Event(models.Model):
    date = models.DateField(("Date"), default=datetime.date.today)
    location = models.ForeignKey('''working with geo location''')



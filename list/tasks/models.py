
#CREATING OUR MODELS HERE and ADDING DATE

from django.db import models
#from datetime import datetime, date
import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add= True)
    date_post = models.DateField(auto_now_add = True)

    def __str__(self):

        return self.title + " --------------> date: "  + str(dt_mtn.strftime('%B %d, %Y'))

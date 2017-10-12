from django.db import models
from django.core.mail import send_mail, EmailMessage

# Create your models here.


class Branch(models.Model):
	name = models.CharField("Name", max_length=30)

	def __str__(self):
		return self.name

class Event(models.Model):
    department = models.ForeignKey(Branch)
    name = models.CharField("Name", max_length=30)
    event_code = models.CharField("event_code", max_length=20)
    price = models.IntegerField("Price", default=0)

    def __str__(self):
    	return self.name


class Participants(models.Model):
	MODE_CHOICES = {('P',"PayTM"), ('C', "Cash")}
	
	event = models.ForeignKey(Event, related_name='participants', null=True, blank=True)
	name = models.CharField("Name", max_length=30)
	phone_no = models.CharField("Phone Number", max_length=12)
	email = models.EmailField()
	mode = models.CharField(choices=MODE_CHOICES, max_length=1)

	def __str__(self):
		return self.phone_no

	def save(self, *args, **kwargs):
        # Add email and sms here, send self.pk

    	email = EmailMessage(
                'BMSIT TECH TRANSFORM', 
                'Hi,' + self.name + '\n\n' +'Thanks for registering for ' + self.event.name + ' at Tech Transform 2017. Please provide thi code for participating. Your secret code is' + random_otp + '\n\nThanks,\nTeam Tech Transform, BMSIT' , 
                'Tech Transform <ankit@bmsit.in>',  
                [self.email],
                )
    	email.send()

        super(Model, self).save(*args, **kwargs)



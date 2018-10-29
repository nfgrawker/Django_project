from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    INSURANCE_CHOICES = (
        ('Life', (
            ('term', 'Term'),
            ('full', 'Full'),
        )
         ),
        ('Auto', (
            ('sixmonth', 'Six Month'),
            ('monthly', 'Monthly'),
        )
         ),
        ('Home',(
            ("escrow","Escrow"),
            ("fullyear","Full Year"),
            ("sixmonth", 'Six Month')
        )
         ),
    )
    client = models.CharField(max_length=100)
    insurance_type = models.CharField(max_length=100, choices=INSURANCE_CHOICES)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    employee = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        template = '{0.client} {0.insurance_type} {0.amount}'
        return template.format(self)


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
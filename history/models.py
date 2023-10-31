from django.db import models
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User



trade_resul_list = [
    ('SUCCESS', 'Success'),
    ('FAILED', 'Failed')
]

trade_type_list = [
    ('LONG', 'Long'),
    ('SHORT', 'Short')
]


class Trade(models.Model):
    chart_day = models.ImageField(upload_to='charts/day')
    chart_hour = models.ImageField(upload_to='charts/hour')
    chart_close = models.ImageField(upload_to='charts/close')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    trade_type = models.CharField(max_length=10, choices = trade_type_list)
    entry_price = models.FloatField()
    stop = models.FloatField()
    tp_1 = models.FloatField()
    tp_2 = models.FloatField(blank=True)
    profit_or_loss = models.FloatField()
    trade_result = models.CharField(max_length=10, choices = trade_resul_list)
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.trade_type} -- {self.trade_result}"
    
    def save(self, *args, **kwargs):
        if self.trade_result == "FAILED":
            self.profit_or_loss = self.profit_or_loss * -1
        super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse("trade_detail", kwargs = {'pk' : self.pk})
    
    def save(self):
        super().save()

        img = Image.open(self.chart_day.path)

        if img.height > 400 or img.width > 600:
            output_size = (400, 600)
            img.thumbnail(output_size)
            img.save(self.chart_day.path)

    def save(self):
        super().save()

        img = Image.open(self.chart_hour.path)

        if img.height > 400 or img.width > 600:
            output_size = (400, 600)
            img.thumbnail(output_size)
            img.save(self.chart_hour.path)

    def save(self):
        super().save()

        img = Image.open(self.chart_close.path)

        if img.height > 400 or img.width > 600:
            output_size = (400, 600)
            img.thumbnail(output_size)
            img.save(self.chart_close.path)
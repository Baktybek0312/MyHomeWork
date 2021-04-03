from django.db import models


class Wish(models.Model):
    text = models.TextField(blank=False, unique=True)
    is_active = models.BooleanField(default=True, null=False)
    order_num = models.IntegerField(default=0)

    def __str__(self):
        return self.text


class CategoryGift(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    order_num = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    phone_number = models.CharField(max_length=12, unique=True, blank=False, default=True)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number


class Request(models.Model):
    sender = models.ForeignKey(Subscriber, on_delete=models.DO_NOTHING, related_name='senders')
    recipient = models.ForeignKey(Subscriber, on_delete=models.DO_NOTHING, related_name='recipients',default=True)
    wish = models.ForeignKey(Wish, on_delete=models.DO_NOTHING, default=True)
    add_date = models.DateTimeField(auto_now_add=True)
    gifts = models.ManyToManyField('Gift')


class Gift(models.Model):
    name = models.CharField(blank=False, max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    category_id = models.ForeignKey(CategoryGift, on_delete=models.DO_NOTHING, default=True)
    price = models.FloatField(default=0, null=False)

    def __str__(self):
        return self.name

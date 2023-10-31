from history.models import Trade
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender = Trade)
def created_trade(sender, instance, created, **kwargs):
    if created:
        return

    user = instance.user
    profile = Profile.objects.get(user=user)

    # Calculate total trades
    profile.total_trades += 1

    # Calculate successful trades
    if instance.trade_result == 'SUCCESS':
        profile.successful_trades += 1

    # Calculate failed trades
    else:
        profile.failed_trades += 1

    # Calculate win rate
    profile.win_rate = profile.successful_trades / profile.total_trades * 100

    # Save profile
    profile.save()


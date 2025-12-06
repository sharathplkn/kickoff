from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='logo/',null=True)
    purse_remaining = models.IntegerField(default=1000)

    captain = models.OneToOneField(
        'Player',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='captain_of_team'   # unique name added
    )

    def __str__(self):
        return self.team_name


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True,related_name='players')
    name = models.CharField(max_length=100)
    card_image = models.ImageField(upload_to='player_cards/',null=True)
    sold_price = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Player: {self.name}"
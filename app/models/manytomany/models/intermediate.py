from django.db import models

__all__ = (
    'Person',
    'Group',
    'Membership',
)

class Person(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=120)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='persons'
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    recommender = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='membership_recommender',
        blank=True,
        null=True,
    )
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return '{person} - {group} ({date})'.format(
            person = self.person.name,
            group = self.group.name,
            date = self.date_joined,
        )
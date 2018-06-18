from django.db import models


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name

    def show_friends(self):

        result = ''
        result += '{}의 친구목록'.format(self.name)
        for fri in self.friends:
            result += '{}'.format(fri.name)

        print(result)
from django.db import models

class TwitterUser(models.Model):
    '''
    User간의 관계는 2종류로 나뉨
      follow
      block

      관계를 나타내는 Relation클래스 사용
    '''
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
    )

    def __str__(self):
        return self.name

    @property
    def following_relations(self):
        # 내가 팔로우 하고 있는 Relation들을 리턴
        '''string = '내가 팔로우 하고 있는 유저 : '
        followings = self.relations_by_from_user.filter(relation_type='f')
        for follo in followings:
            string += follo.from_user.name'''
        return self.relations_by_from_user.filter(relation_type='f')

    @property
    def block_relations(self):
        return self.relations_by_from_user.filter(relation_type='b')

    @property
    def follower_relations(self):
        return self.relations_by_to_user.filter(relation_type='f')



class Relation(models.Model):
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )

    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            self.get_relation_type_display(),
        )


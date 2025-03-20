from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 


CHAR_DEFAULT_MAX_LENGTH = 20

class CustomerBot(models.Model):
    '''
    客人役のボットデータ最上部
    '''
    name = models.CharField(max_length=20)


    def __str__(self):
        return self.name



class CustomerBotFlow(models.Model):
    '''
    客人役の対話フロー
    '''
    customer_bot_id = models.ForeignKey(CustomerBot, on_delete=models.CASCADE)
    my_flow_id = models.IntegerField(default=0)

    nega_point = models.IntegerField(
        default=0,
        choices={-1: -1, 0: 0, 1: 1}
    )
    neut_point = models.IntegerField(
        default=0,
        choices={-1: -1, 0: 0, 1: 1}
    )
    posi_point = models.IntegerField(
        default=0,
        choices={-1: -1, 0: 0, 1: 1}
    )

    nega_branch = models.IntegerField(
        validators=[MinValueValidator(-1), MaxValueValidator(100)], default=0)
    neut_branch = models.IntegerField(
        validators=[MinValueValidator(-1), MaxValueValidator(100)], default=0)
    posi_branch = models.IntegerField(
        validators=[MinValueValidator(-1), MaxValueValidator(100)], default=0)

    front_customer_utt = models.TextField(
        max_length=CHAR_DEFAULT_MAX_LENGTH,default='', blank=True)
    s1_back_customer_utt = models.TextField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='', blank=True)
    s2_back_customer_utt = models.TextField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='', blank=True)
    s3_back_customer_utt = models.TextField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='', blank=True)


    def __str__(self):
        return str(self.customer_bot_id) + '_' + str(self.my_flow_id)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['customer_bot_id', 'my_flow_id'],
                name='flow_unique'
            )
        ]



class MerchantBot(models.Model):
    '''
    商人役のボットデータ最上部
    '''
    name = models.CharField(max_length=20)
    clear_conciliation_point = models.IntegerField(default=0)



class MerchantBotBrain(models.Model):
    '''
    商人役の行動選択ルール
    '''
    merchant_bot_id = models.ForeignKey(MerchantBot, on_delete=models.CASCADE)
    main_cmd = models.CharField(max_length=CHAR_DEFAULT_MAX_LENGTH)
    priority = models.IntegerField(default=0)


class Conduct(models.Model):
    '''
    行動選択肢データの最上部
    '''
    display_name = models.CharField(max_length=20, default='表示用の名前')
    meta_name = models.CharField(max_length=20, default='function name only')
    rate = models.IntegerField(default=1)
    note = models.TextField(default='ここに説明を追加')


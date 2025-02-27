from django.db import models


CHAR_DEFAULT_MAX_LENGTH = 20

class CustomerBot(models.Model):
    '''
    客人役のボットデータ最上部
    '''
    name = models.CharField(max_length=20)
    persona_status1 = models.CharField()

    def __str__(self):
        return self.name



class CustomerBotFlow(models.Model):
    '''
    客人役の対話フロー
    '''
    customer_bot_id = models.ForeignKey(CustomerBot, on_delete=models.CASCADE)
    my_flow_id = models.IntegerField()
    front_customer_utt = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH,
        default='客役の冒頭発話'
    )

    hint_purpose = models.CharField()
    hint_relation = models.CharField()
    hint_support = models.CharField()

    s1_back_customer_utt = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='客役の事後発話1')
    s2_back_customer_utt = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='客役の事後発話2')
    s3_back_customer_utt = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='客役の事後発話3')
    s1_branch = models.IntegerField()
    s2_branch = models.IntegerField()
    s3_branch = models.IntegerField()


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


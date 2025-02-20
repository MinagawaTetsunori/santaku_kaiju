from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)






class CustomerBot(models.Model):
    '''
    客人役のボットデータ最上部
    '''
    name = models.CharField(max_length=20)


class MerchantBot(models.Model):
    '''
    商人役のボットデータ最上部
    '''
    name = models.CharField(max_length=20)
    clear_conciliation_point = \
        conciliation_add_point = models.IntegerField(default=0)


class CustomerBotFlow(models.Model):
    '''
    客人役の対話フロー
    '''
    customer_bot_id = models.ForeignKey(CustomerBot, on_delete=models.CASCADE)
    talk_text = models.CharField(max_length=20)


class CustomerBotFlowSantaku(models.Model):
    '''
    客人役に対する商人の三択
    '''
    customer_bot_flow_id = \
        models.ForeignKey(CustomerBotFlow, on_delete=models.CASCADE)
    conciliation_add_point = models.IntegerField()  # 懐柔(ゲームでは怪柔)


class MerchantBotBrain(models.Model):
    '''
    商人役の行動選択ルール
    '''
    merchant_bot_id = models.ForeignKey(CustomerBot, on_delete=models.CASCADE)
    main_cmd = models.CharField(max_length=20)
    priority = models.IntegerField()


class Conduct(models.Model):
    '''
    行動選択肢データの最上部
    '''
    display_name = models.CharField(max_length=20, '表示用の名前')
    meta_name = models.CharField(max_length=20, 'function name only')
    rate = models.IntegerField(default=1)
    note = models.TextField(default='ここに説明を追加')


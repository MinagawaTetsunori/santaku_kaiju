from django.db import models


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
    talk_text = models.CharField(max_length=CHAR_DEFAULT_MAX_LENGTH)

    # sはsantakuの頭文字
    s1_name = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='選択肢名1')
    s1_conciliation_add_point = models.IntegerField(default=0)  # 懐柔(ゲームでは怪柔)
    s1_res = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='客役の応答1')
    s1_branch = models.IntegerField(default=0)
    s2_name = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='選択肢名2')
    s2_conciliation_add_point = models.IntegerField(default=0)
    s2_res = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='客役の応答2')
    s2_branch = models.IntegerField(default=0)
    s3_name = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='選択肢名3')
    s3_conciliation_add_point = models.IntegerField(default=0)
    s3_res = models.CharField(
        max_length=CHAR_DEFAULT_MAX_LENGTH, default='客役の応答3')
    s3_branch = models.IntegerField(default=0)


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


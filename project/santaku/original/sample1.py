import random

# HINT_KAIJU_POINTS = {
#     '目的': {
#         '修復': {'nega': 0, 'neut': 0, 'posi': 0},
#         '成長': {'nega': 0, 'neut': 1, 'posi': 0},
#         '復讐': {'nega': 1, 'neut': 1, 'posi': 0}
#     },
#     '対象者': {
#         '自分': {'nega': 0, 'neut': 0, 'posi': 0},
#         '親しい人': {'nega': 1, 'neut': 0, 'posi': 1},
#         'その他': {'nega': 1, 'neut': 0, 'posi': 0}
#     },
#     '要求対応': {
#         '共感': {'nega': 0, 'neut': 0, 'posi': 0},
#         'アドバイス': {'nega': 0, 'neut': 1, 'posi': 1},
#         '後押し': {'nega': 0, 'neut': 0, 'posi': 1}
#     }
# }

# USER_TYPE = {
#     'ポジティブ': {'need': 'posi'},
#     'ニュートラル': {'need': 'neut'},
#     'ネガティブ': {'need': 'nega'}
# }


def gacha_ability(keeped_ability: dict[str, int]) -> list[str]:
    '''
    レベルが上がった時のアビリティ抽選
    ユーザーに選ばせるアビリティを三択で出力
    '''
    # 数値が高いほど排出率が高い, class別途で作った方がいいかも
    emissions = {
        'hint_purpose_repair': 5,
        'hint_purpose_grows': 5,
        'hint_purpose_revenge': 5,
        'hint_relation_myself': 5,
        'hint_relation_important': 5,
        'hint_relation_other': 5,
        'hint_support_empathy': 5,
        'hint_support_advice': 5,
        'hint_support_boost': 5
    }

    emissions = {
        k: emissions[k] - keeped_ability[k] for k in emissions
    }

    # emissionの残数分keyを排出abilioty名として格納
    emission_names = []
    for k in emissions:
        emission_names += [k for _ in range(emissions[k])] 
    
    random.shuffle(emission_names)

    MAX_EMISSION = 3
    if len(emission_names) == MAX_EMISSION:
        return emission_names[:MAX_EMISSION]
    else:
        return emission_names
    


def game():
    '''
    ゲームのメイン部分
    '''
    # 客役のサンプルフロー
    SCENARIO_FLOW = [
        {
            'event_id': 1,
            'utt': 'aaaa',
            'hints': {'purpose': '', 'relation': '', 'support': ''},
            'branch':{
                'nega': {
                    'customer_response_utt': 'aaa',
                    'jump_event_id': 0
                },
                'neut': {},
                'posi': {}
            }
        }
    ]



class Merchant:
    def __init__(self, name: str):
        self.name = name
        self.rules: list[self.Rule] = [self.Rule()]
    
    def add_empty_rule(self) -> None:
        self.rules.Add(self.Rule())

    class Rule:
        def __init__(self):
            self.output_santaku: str = 'neut'
            self.conditions: list[self.Condition] = []

    class Condition:
        def __init__(self):
            self.left_val = 'neut'
            self.right_val = 'neut'
            self.operator = '=='
        
        def set_elm(self, key_name: str, val_name: str) -> None:
            SIDE_VALS = ['nega', 'neut', 'posi']
            OPE_VALS = []

            match key_name:
                case 'operator':
                    if val_name in OPE_VALS:
                        self.operator = val_name
                    else:
                        raise ValueError('not {val_name} in OPE_VALS')
                case 'left' or 'right':
                    if val_name in SIDE_VALS:
                        if key_name == 'left': self.left_val = val_name
                        if key_name == 'right': self.right_val = val_name
                    else:
                        raise ValueError('not {val_name} in SIDE_VALS')
                case _:
                    raise ValueError('not {key_name} in KEYS')
            


if __name__=='__main__':
    merchant = Merchant('AA')
    print(merchant.rules[0].output_santaku)

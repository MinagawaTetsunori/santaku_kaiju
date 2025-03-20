import random
    import MySQLdb


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
    def __init__(self, name: str = 'unknown'):
        self.name = name
        self.bounus_santaku = 'neut'
        self.bullets: list[self.Bullet] = [self.Bullet()]
    
    def add_new_bullet(self) -> None:
        self.bullets.Add(self.Bullet())
    
    def shoot_bullet(self, customer_id: int, flow_id: int) -> str:
        '''
        客役idとflow_idで現状を指定したら商人役の行動を返す
        '''
        output_santaku: str = 'neut'

        for bullet in self.bullets:
            output_santaku = bullet.output_santaku
            left_val: float = calc_scval()
            left_val: float = calc_scval()
            is_shoot: bool = True
            for cond in conds:
                match cond.operator:
                    case '==':
                        if left_val == right_val: continue
                    case '<':
                        if left_val < right_val: continue
                    case '>':
                        if left_val > right_val: continue
                    case _:
                        raise ValueError('not cond operater')
                is_shoot = False
                break

        return output_santaku
    
    def calc_scval() -> float:
        return 0.0

    class Bullet:
        def __init__(self):
            self.output_santaku: str = 'neut'
            self.conds: list[ShootingCondition] = [Merchant.ShootingCondition()]
        
        def add_new_shooting_cond() -> None:
            '''
            新規のshoting_condを生成してcondsに追加
            '''
            self.conds.Add(ShootingCondition())
        
        # def is_shoot() -> bool:
        #     '''
        #     このBulletが現在の客役idとflow_idにおいて条件を満たすか返す
        #     '''
        #     for shooting_condition in self.conds:
        #         return False
        #     return True

    class ShootingCondition:
        def __init__(self):
            self.left_val = 'neut'
            self.right_val = 'neut'
            self.operator = '=='
        
        def set_elm(self, key_name: str, val_name: str) -> None:
            SIDE_VALS = ['nega', 'neut', 'posi']
            OPE_VALS = ['==', '<', '>']

            match key_name:
                case 'operator':
                    if val_name in OPE_VALS:
                        self.operator = val_name
                    else:
                        raise ValueError('not {val_name} in OPE_VALS')
                case 'left'|'right':
                    if val_name in SIDE_VALS:
                        if key_name == 'left': self.left_val = val_name
                        if key_name == 'right': self.right_val = val_name
                    else:
                        raise ValueError('not {val_name} in SIDE_VALS')
                case _:
                    raise ValueError('not {key_name} in KEYS')
            


if __name__=='__main__':
    # merchant = Merchant('AA')
    # print(merchant.shoot_bullet(0, 0))
    connection = MySQLdb.connect(
        host='db',
        user='root',
        passwd='root',
        db='santaku_db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM santaku_customerbotflow')
    rows = cursor.fetchall()
    print(rows)
    connection.close()

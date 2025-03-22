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
        DEFAULT_SANTAKU = 'neut'
        output_santaku: str = DEFAULT_SANTAKU

        for bullet in self.bullets:
            output_santaku = bullet.output_santaku
            is_shoot: bool = True
            for cond in conds:
                left_num: float = calc_scval(customer_id, flow_id, cond.left_cmd)
                right_num: float = calc_scval(customer_id, flow_id, cond.right_cmd)
                match cond.operator:
                    case '==':
                        if left_num == right_num: continue
                    case '<':
                        if left_num < right_num: continue
                    case '>':
                        if left_num > right_num: continue
                    case _:
                        raise ValueError('not cond operater')
                is_shoot = False
                break

        return output_santaku
    
    def calc_scval(customer_id: int, flow_id: int, calc_cmd: str) -> float:
        '''
        左右の変数を計算方法を指定した後に計算して返す
        '''
        connection = MySQLdb.connect(
            host='db',
            user='root',
            passwd='root',
            db='santaku_db')
        cursor = connection.cursor()
        rslt_scval: float = 0.0

        match calc_cmd:
            case 'nega'|'neut'|'posi':
                cursor.execute(
                    'SELECT {calc_cmd}_point FROM santaku_customerbotflow')
                rslt_scval = float(cursor.fetchone()[0])
            case _:
                pass

        connection.close()
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


    class ShootingCondition:
        def __init__(self):
            self.left_cmd = 'neut'
            self.right_cmd = 'neut'
            self.operator = '=='
        
        def set_elm(self, key_name: str, cmd_name: str) -> None:
            SIDE_CMDS = ['nega', 'neut', 'posi', 'random']
            OPE_CMDS = ['==', '<', '>']

            match key_name:
                case 'operator':
                    if cmd_name in OPE_CMDS:
                        self.operator = cmd_name
                    else:
                        raise ValueError('not {cmd_name} in OPE_CMDS')
                case 'left'|'right':
                    if cmd_name in SIDE_CMDS:
                        if key_name == 'left': self.left_cmd = cmd_name
                        if key_name == 'right': self.right_cmd = cmd_name
                    else:
                        raise ValueError('not {cmd_name} in SIDE_CMDS')
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
    cursor.execute('SELECT posi_point FROM santaku_customerbotflow')
    rows = cursor.fetchone()[0]
    print(rows)
    connection.close()

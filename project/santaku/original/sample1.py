import random
import MySQLdb

'''
主にコンソール上での機能テストを行う
'''


def game():
    '''
    ゲームのメイン部分
    1回分
    '''
    # 1.商人役を作る
    merchant = Merchant('商人A')
    merchant.keeped_abilities = {'posi': 1, 'const_1': 1}

    # 2.最初のmind編集
    merchant.edit_mind()

    # 3.客役1人とコミュ
    # 4.ガチャ1回
    # 5.再編集
    # 6.終了(続きはまた今度)


def gacha_ability(keeped_abilities: dict[str, int]) -> list[str]:
    '''
    レベルが上がった時のアビリティ抽選
    ユーザーに選ばせるアビリティを三択で出力
    '''
    # 数値が高いほど排出率が高い
    EMISSIONS = {
        'nega': 5, 'neut': 5, 'posi': 5, 
        'random': 5, 
        'const_-1': 5, 'const_0': 5, 'const_1': 5
    }

    emissions = {
        k: EMISSIONS[k] - keeped_abilities[k] for k in EMISSIONS
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
    


class Merchant:
    def __init__(self, name: str = 'unknown'):
        self.name = name
        self.bounus_santaku = 'neut'
        self.bullets: list[self.Bullet] = [self.Bullet()]
        self.keeped_abilities: dict[str, int] = {}


    def edit_mind(self) -> None:
        '''
        コンソール上でmind編集する用
        '''
        # 1.変更するcmdをbullet>cond>cmdの順で選択
        # 1.1.今あるbulletの数を表示
        print(f'stock_bullets: {len(self.bullets)}')
        choice_bullet_idx: str = input('choice_bullet_idx(stasrt=0): ')
        # 
        # 2.選択肢の番号を入力して変更完了

    
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
    
    def calc_scval(self, customer_id: int, flow_id: int, calc_cmd: str) -> float:
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
                    f'''
                    SELECT {calc_cmd}_point FROM santaku_customerbotflow 
                    WHERE 
                    customer_bot_id = {customer_id} and 
                    my_flow_id = {flow_id}
                    ''')
                rslt_scval = float(cursor.fetchone()[0])
            case 'const_-1'|'const_0'|'const_1':
                rslt_scval = float(calc_cmd.replace('const_', ''))
            case 'random':
                items: list[str] = ['nega', 'neut', 'posi']
                cursor.execute(
                    f'''
                    SELECT {random.choices(items)}_point 
                    FROM santaku_customerbotflow 
                    WHERE 
                    customer_bot_id = {customer_id} and 
                    my_flow_id = {flow_id}
                    ''')
                rslt_scval = float(cursor.fetchone()[0])
            case _:
                pass

        connection.close()
        return rslt_scval


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
            SIDE_CMDS = [
                'nega', 'neut', 'posi', 'random', 
                'const_-1', 'const_0', 'const_1'
            ]
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
                        elif key_name == 'right': self.right_cmd = cmd_name
                    else:
                        raise ValueError('not {cmd_name} in SIDE_CMDS')
                case _:
                    raise ValueError('not {key_name} in KEYS')
            


if __name__=='__main__':
    game()

    # merchant = Merchant('AA')
    # print(merchant.calc_scval(1, 0, 'nega'))

    # connection = MySQLdb.connect(
    #     host='db',
    #     user='root',
    #     passwd='root',
    #     db='santaku_db')
    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM santaku_customerbotflow')
    # rows = cursor.fetchall()
    # print(rows)
    # connection.close()

import random

HINT_KAIJU_POINTS = {
    '目的': {
        '修復': {'nega': 0, 'neut': 0, 'posi': 0},
        '成長': {'nega': 0, 'neut': 1, 'posi': 0},
        '復讐': {'nega': 1, 'neut': 1, 'posi': 0}
    },
    '対象者': {
        '自分': {'nega': 0, 'neut': 0, 'posi': 0},
        '親しい人': {'nega': 1, 'neut': 0, 'posi': 1},
        'その他': {'nega': 1, 'neut': 0, 'posi': 0}
    },
    '要求対応': {
        '共感': {'nega': 0, 'neut': 0, 'posi': 0},
        'アドバイス': {'nega': 0, 'neut': 1, 'posi': 1},
        '後押し': {'nega': 0, 'neut': 0, 'posi': 1}
    }
}

USER_TYPE = {
    'ポジティブ': {'need': 'posi'},
    'ニュートラル': {'need': 'neut'},
    'ネガティブ': {'need': 'nega'}
}


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
    FLOW = [
        {'talk': 'aaaa', 'santaku': ['a', 'b', 'c']}
    ]



if __name__=='__main__':
    game()
    print('hello')
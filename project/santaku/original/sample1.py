# 1体分

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
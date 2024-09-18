class Config:
    screen_size = (screen_width, screen_height) = 800, 600
    title = '扫雷'
    FPS = 60
    images = {
        "icon": 'images/icon.ico',
        '0': 'images/0.png',
        "1": 'images/1.png',
        "2": 'images/2.png',
        "3": 'images/3.png',
        "4": 'images/4.png',
        "5": 'images/5.png',
        "6": 'images/6.png',
        "7": 'images/7.png',
        "8": 'images/8.png',
        'boom': 'images/boom.png',
        'flag': 'images/flag.png',
        'unknown': 'images/unknown.png',
    }

    button_text = {
        '1': '开始/暂停',
        '2': '更改难度',
        '3': '历史记录'
    }

    button_scale = {
        '1w': 25,
        '1h': 60,
        '1f': 30,
    }

    button_parameter = {
        'x': int(screen_width / button_scale['1w']),
        'y': int(screen_height / button_scale['1h']),
        'f': int(screen_height / button_scale['1f']),
    }

    button_color = {
        'nc': (200, 200, 200),
        'sc': (100, 100, 100)
    }

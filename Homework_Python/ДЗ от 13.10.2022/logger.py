from datetime import datetime as dt

def info_data(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{time} совершено действие: {data} = ')

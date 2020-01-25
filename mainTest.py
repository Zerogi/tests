from flask import Flask
from flask import request
import json
from json import dumps, loads

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def main():
    print(0)
    ## Создаем ответ
    response = {
        'session': request.json['session'],
        'version': request.json['version'],  # не очень нужная строка
        'response': {
            'end_session': False
        }
    }
    ## Заполняем необходимую информацию
    print(11)
    handle_dialog(response, request.json)
    return json.dumps(response)


def handle_dialog(res,req):
    print(0)
    if req['request']['original_utterance']:
        ## Проверяем, есть ли содержимое
        res['response']['text'] = req['request']['original_utterance']
    else:
        ## Если это первое сообщение — представляемся
        res['response']['text'] = "Я echo-bot, повторяю за тобой"

if __name__ == '__main__':
    print('START')
    app.run()
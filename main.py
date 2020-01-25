from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/post', methods=['POST'])
def main():
    #создаю ответ
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    start(response, request.json)
    return json.dumps(response)


def start(res, req):
    if not req['request']['original_utterance']:
        res['response']['text'] = 'Привет. Хочешь пройти опрос?'
    else:
        print(req['request']['command'])
        if 'да' in req['request']['command'].lower():
            res['response']['text'] = 'Тогда начнем'
            return json.dumps(res)
        else:
            res['response']['end_session'] = True
            return json.dumps(res)


if __name__ == '__main__':
    print('START')
    app.run()
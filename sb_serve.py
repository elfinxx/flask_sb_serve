from flask import Flask, request, json
from slacker import Slacker
from card_handler import save_spend_data_form_360_reward_card

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/spend', methods=['POST'])
def add_spending_data():
    spend_data = save_spend_data_form_360_reward_card(json.loads(request.data))

    with open("token", 'r', encoding='utf8') as f:
        for line in f:
            token = line

    if "이*민" in spend_data[2]:
        user_name = "bart"
    else:
        user_name = "sara"

    r_msg = '{}가 {}에서 {} 썼습니다.'.format(user_name, spend_data[1], spend_data[0])
    slack = Slacker(token)
    slack.chat.post_message('#mony', r_msg, as_user=True)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

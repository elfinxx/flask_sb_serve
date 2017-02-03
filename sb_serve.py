from flask import Flask, request, json
from slacker import Slacker
from card_handler import save_spend_data_form_360_reward_card

app = Flask(__name__)
with open("token", 'r', encoding='utf8') as f:
    for line in f:
        token = line

slack = Slacker(token)

@app.route('/')
def hello_world():
    txt = "[Web발신]\n \
    [체크.승인]\n \
    10,000원\n \
    SC은행BC(0363)이*민님\n \
    01/31 21:42\n \
    통장잔액2,580,687원\n \
    씨유판교신"
    save_spend_data_form_360_reward_card(txt)
    return 'Hello World!'


@app.route('/spend', methods=['POST'])
def add_spending_data():
    r_msg = save_spend_data_form_360_reward_card(json.loads(request.data))
    slack.chat.post_message('#mony', r_msg, as_user=True)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

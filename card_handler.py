from pymongo import MongoClient


def save_spend_data_form_360_reward_card(txt):
    spend_data = txt.split('\n')
    # print(spend_data)
    cost = spend_data[2]
    spend_time = spend_data[4]
    shop = spend_data[6]

    print(cost, spend_time, shop)

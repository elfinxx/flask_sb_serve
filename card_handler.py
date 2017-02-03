import pymysql


def save_spend_data_form_360_reward_card(txt):
    spend_data = txt.split('\n')
    cost = spend_data[2]
    user = spend_data[3]
    spend_time = spend_data[4]
    # shop = spend_data[6]
    shop = "TEST"
    reformatted_cost = cost.replace(',', '').replace('원', '')

    connection = pymysql.connect(host='mony.cbt6ak6cjhvc.ap-northeast-2.rds.amazonaws.com',
                                 user='sb',
                                 password='a12345678',
                                 db='mony',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `history` (`cost`, `type`, `fullmsg`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (reformatted_cost, shop, txt))
        connection.commit()
        return cost, shop, user

    finally:
        connection.close()

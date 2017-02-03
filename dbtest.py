import pymysql.cursors
import time

connection = pymysql.connect(host='mony.cbt6ak6cjhvc.ap-northeast-2.rds.amazonaws.com',
                             user='sb',
                             password='a12345678',
                             db='mony',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        time.strftime('%Y-%m-%d %H:%M:%S')

        # Create a new record
        sql = "INSERT INTO `history` (`cost`, `type`, `fullmsg`) VALUES (%s, %s, %s)"
        cursor.execute(sql, ('123', '씨유', '웹발신'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `history`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

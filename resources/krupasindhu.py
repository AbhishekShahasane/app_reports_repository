import mysql.connector
from flask_restful import Resource

mydb = mysql.connector.connect(
    host="203.192.211.193",
    user="KCAL_USR",
    passwd="bapu18112025"
)


class krupasindhuData(Resource):
    def get(self):
        connection = mydb
        cursor = connection.cursor()
        total_device_query = "SELECT count(distinct(DEVICE_ID)) FROM KRUPASINDHU_CAL_DB.EVENT_LOG where ACTIVITY_TYPE='TERMSCONDDEVICE'"
        cursor.execute(total_device_query)
        result1 = cursor.fetchone()

        total_device_query = "SELECT count(*) FROM KRUPASINDHU_CAL_DB.USER_MASTER"
        cursor.execute(total_device_query)
        result2 = cursor.fetchone()

        total_device_query = "SELECT COUNT(*) FROM KRUPASINDHU_CAL_DB.NOTES"
        cursor.execute(total_device_query)
        result3 = cursor.fetchone()

        total_device_query = "SELECT COUNT(*) FROM KRUPASINDHU_CAL_DB.REMINDERS"
        cursor.execute(total_device_query)
        result4 = cursor.fetchone()

        total_reports = [result1[0], result2[0], result3[0], result4[0]]

        return total_reports

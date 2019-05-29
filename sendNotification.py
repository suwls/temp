# -*- coding: utf-8 -*- 

import pyfcm
import pymysql
import sys

# AI 결과값: 이름 or Stranger

# ID 이용해서 Token 가져오기
def getToken(id):
	conn = pymysql.connect(host='localhost', user='app', password='Kookmin1!', db='db', charset='utf8')
	curs = conn.cursor()

	sql = "select token from Login where id=%s"
	curs.execute(sql,id)

	token = "empty"
	rows = curs.fetchall()
	if len(rows) == 1:
		token = rows[0][0]
		print(token)
	else:
		print("등록된 토큰이 없습니다")

	return token

# 알림 전송하기
def send(id, visitor):
	push_service = pyfcm.FCMNotification(api_key = "AAAAY8kbeM8:APA91bGq5bf_ALyJu6ADYnxna_Ggh-KRTzZUS-NY6c6CxuTxe7G-3zYnLnE_LFyO9kpAvrZPx8SuY7XM847_38uRX5JICC9B7Kr8pP-o_u0TbKB0JN4i7u5JMe9CbEwMJr5lmjaKrCTI")
#	message_title = "방문자 알림"
	message_body = visitor + "님이 방문했습니다"
	registration_id = getToken(id)

	data = {"title" : "BANG BANG 방문자 알림",
		"body" : message_body,
		}
	if registration_id != "empty":
		result = push_service.notify_single_device(registration_id=registration_id, data_message=data)
#		result = push_service.notify_single_device(registration_id=registration_id, message_title = message_title, message_body = message_body, data_message = data)
		print(result)
	else:
		print("등록된 기기가 없습니다.")

#visitor 알림 여부 받아오기 
def getStatus(id, visitor):
	conn = pymysql.connect(host='localhost', user='admin', password='Kookmin1!', db='db', charset='utf8')
	curs = conn.cursor()

	sql = "select * from Acquaintance where id=%s and name=%s"
	curs.execute(sql, (id, visitor))

	rows = curs.fetchall()

	alarm = 1
	#외부인일 경우 알림 발송
	if len(rows) == 0:
		alarm = 1
	#지인일 경우 사용자의 알림 수신 여부에 따라 발송 
	elif len(rows) == 1:
		alarm = rows[0][4]

	return alarm

if __name__ == '__main__':
	visitor = sys.argv[1]
	id = sys.argv[2]
	alarm = getStatus(id, visitor)
	if(alarm):
		send(id,visitor)

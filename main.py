import requests
import time

#Gets token value from .env file, you can also use token = *your token goes here*
#Получает токен из файла .env, можно так же использовать token = *ваш токен*
token = #your token goes here

#Specify time to wait between changes (must be more than 60 otherwise you can get ban by vk)
#Время между изменением статуса (должно быть больше чем 60 секунд, иначе вы можете получить бан от вк)
def wait():
  time.sleep(60)

#Method to set status, where text is text to be place in status and token is your page token
#Метода для установки статуса, где text - текст в статус, token - токен вашей страницы в вк
def setStatus(text):
  requests.get(f'https://api.vk.com/method/status.set?text={text}&access_token={token}&v=5.131')

#Program starts here. Be free with your ideas :)
#Тут выполняется изменение статуса. Ставьте что угодно <3
while True:
  setStatus("Text_1")
  wait()
  setStatus("Текст_2")
  wait()
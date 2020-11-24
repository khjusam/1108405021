import requests

  def lineNotifyMessage(token, msg):
      headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
	
      payload = {'message': msg}
      r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
      return r.status_code
	
  # 修改為你要傳送的訊息內容
  message = 'Notify from LINE, HELLO WORLD'
  # 修改為你的權杖內容
  token = 'b3wPJEnF56Y2QPhhrXPOupFuRrgypwRkwxtq9x5OQcN'

  lineNotifyMessage(token, message)
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# import sys
# sys.path.append("./secret")

# from secret import CHANNEL_ACCESS_TOKEN,CHANNEL_SECRET




app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi("QUPfXCz2i+hT5J7lTycNpv8e8FbeipBqMQxZZY1sgju9FVcyu3pfdxhC80cI+uErfqX3LtoFzLKmkbPB+r+WPBPM2g+SJHzhUrzzoIye2S+obwII6STUPtnExg+UR9oxPfQgAlRnbeUlAdiotZ0qxAdB04t89/1O/w1cDnyilFU=")
# Channel Secret
handler = WebhookHandler("99fe0d594fb9d40f3ef5ac088bee8517")

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

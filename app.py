from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('1sGgoPAJ5EAroYd+ZNs/Ixe+y+yIHC2xev1gvg41ErBNaZERrjUrUkmFH8NEp39mzhPQ8il/TnfPlQw46Cnnu5D/4AjptTq0/3NSUdd7pfdwwRIYdg35rIedvrIKdL1SqU6Qk/8D6U6/1yjjPzvoswdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6e7fba44d9e274e6dd0cee37e1dbf747')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
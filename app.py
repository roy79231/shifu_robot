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
import random

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
    msg = event.message.text
    r = '不好意思，請依照格式輸入，謝謝!'
    x = random.randint(20,80)
    y = x + 20
    if '陳立軒' in msg and '1-1' in msg :
        r = '郁達師傅掐指一算，你這次告白一定成功。'
    elif '陳立軒' in msg and '1-2' in msg :
        r = '郁達師傅有言:在您出生當日執行，會有最高機率成功。'    
    elif '1-1' in msg :
        r = '你有',x,'%的機率會成功，師傅有言：這只是您目前的命運，您依舊能靠你後天努力來提高機率。'
    elif '1-2' in msg :
        r = '郁達師傅說您最適合在下個重要節慶告白,成功機率有到', y ,'%。'
    elif '2-0' in msg :
        r = '此需要更多私人資訊，請洽詢師傅ig:@_stanley_09_01'
    elif '3-0' in msg :
        r = '此需要更多私人資訊，請洽詢師傅ig:@_stanley_09_01'
    elif '4-0' in msg :
        r = '此需要更多私人資訊，請洽詢師傅ig:@_stanley_09_01'
    elif '5-0' in msg :
        r = '此需要更多私人資訊，請洽詢師傅ig:@_stanley_09_01'



    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()
# -*- coding: utf-8 -*-
"""
Date: 2023/11/14
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
"""

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import os
import json

# line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
# handler = WebhookHandler('YOUR_CHANNEL_SECRET')

def lambda_handler(event, context):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):

        event_text = event.message.text

        if event_text == "Hello":
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="World")
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=event_text)
            )

    # get X-Line-Signature header value
    signature = event['headers']['x-line-signature']

    # get request body as text
    body = event['body']

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return {
            'statusCode': 502,
            'body': json.dumps("Invalid signature. Please check your channel access token/channel secret.")
        }
    return {
        'statusCode': 200,
        'body': json.dumps("Hello from Lambda!")
    }
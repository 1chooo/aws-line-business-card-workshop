# -*- coding: utf-8 -*-
"""
Date: 2023/11/14
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Version: v0.1.0
"""

import os
import json
from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import MessageEvent
from linebot.models import TextMessage
from linebot.models import ImageMessage
from linebot.models import TextSendMessage
from linebot.models import ImageSendMessage
from linebot.models import VideoSendMessage
from linebot.exceptions import InvalidSignatureError

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def lambda_handler(event, context):
    @handler.add(MessageEvent, message=TextMessage)
    def handle_text_message(event):

        event_text = event.message.text

        if event_text == "Hello":
            reply_messages = [
                TextSendMessage(
                    text=f'World'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "寶可夢是什麼？":
            reply_messages = [
                TextSendMessage(
                    text=f'在一個充滿奇妙生物的世界裡，有著一種稀有而神秘的存在，那就是寶可夢。這些生物在人們的故事中被描述為可以在各種環境下被發現，有時候出現在草叢中、河邊，甚至是高高的山頂。人們說，能夠與寶可夢建立連結的訓練師，便能體驗到前所未有的奇妙旅程。'
                ),
                TextSendMessage(
                    text=f'寶可夢不僅僅是各種不同形狀和能力的生物，更是一種象徵，象徵著冒險、友誼和夢想。這個充滿著奇妙生物的世界，永遠散發著光芒，等待著有心人的探索與發現。'
                ),
                TextSendMessage(
                    text=f'親愛的訓練家，你準備好踏上旅程了嗎？'
                ),
                ImageSendMessage(
                    original_content_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                    preview_image_url = "https://2023-amazon-ambassador.s3.amazonaws.com/hugo_grad.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 創辦故事":
            reply_messages = [
                TextSendMessage(
                    text=f'我想知道 AWS 創辦故事 1'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 創辦故事 2'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 創辦故事 3'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 創辦故事 4'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/01_story.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/01_story.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 提供的業務":
            reply_messages = [
                TextSendMessage(
                    text=f'我想知道 AWS 提供的業務 1'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 提供的業務 2'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 提供的業務 3'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 提供的業務 4'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/02_business.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/02_business.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 技術背景":
            reply_messages = [
                TextSendMessage(
                    text=f'我想知道 AWS 技術背景 1'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 技術背景 2'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 技術背景 3'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 技術背景 4'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/03_tech.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/03_tech.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 的領導力準則":
            reply_messages = [
                TextSendMessage(
                    text=f'我想知道 AWS 的領導力準則 1'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 的領導力準則 2'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 的領導力準則 3'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 的領導力準則 4'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/04_leadership.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/04_leadership.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 未來的發展方向":
            reply_messages = [
                TextSendMessage(
                    text=f'我想知道 AWS 未來的發展方向 1'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 未來的發展方向 2'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 未來的發展方向 3'
                ),
                TextSendMessage(
                    text=f'我想知道 AWS 未來的發展方向 4'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/05_future.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/05_future.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想了解 AWS LINE BOT 開發團隊":
            reply_messages = [
                TextSendMessage(
                    text=f'我想了解 AWS LINE BOT 開發團隊 1'
                ),
                TextSendMessage(
                    text=f'我想了解 AWS LINE BOT 開發團隊 2'
                ),
                TextSendMessage(
                    text=f'我想了解 AWS LINE BOT 開發團隊 3'
                ),
                TextSendMessage(
                    text=f'我想了解 AWS LINE BOT 開發團隊 4'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/06_developing.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/06_developing.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        else:
            reply_messages = [
                TextSendMessage(
                    text=f'{event_text}'
                ),
            ]
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )


    try:
        # get X-Line-Signature header value
        signature = event['headers']['x-line-signature']

        # get request body as text
        body = event['body']
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

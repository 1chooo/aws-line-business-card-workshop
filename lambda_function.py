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
        elif event_text == "我想知道 AWS 創辦故事":
            reply_messages = [
                TextSendMessage(
                    text=f'當然！AWS（Amazon Web Services）是由亞馬遜公司於2006年推出的雲端運算平台。創辦人Jeff Bezos意識到雲端運算的巨大潛力，於是啟動了AWS的發展。AWS最初的目標是為企業提供可靠、可擴展、經濟實惠的雲端解決方案。這個決策後來改變了整個科技業的格局，使得任何人都能夠在全球運行低成本的應用程序，可見Jeff Bezos的願景和堅持對AWS的成功起到了關鍵作用！'
                ),
                TextSendMessage(
                    text=f'AWS的創辦故事始於2003年，當時亞馬遜公司的Jeff Bezos意識到他們在建設強大的內部基礎設施方面取得了不錯的進展！而這個基礎設施可以成為一個強大的雲端運算平台，能夠為其他企業提供服務。於是在2006年，AWS正式推出，開始提供雲端服務。AWS的成功與其開放性、靈活性和不斷創新的企業文化有關，而這一切都源於Jeff Bezos對技術和未來的敏銳洞察力。'
                ),
                TextSendMessage(
                    text=f'AWS的創辦故事始於2003年，當時亞馬遜公司內部建立了一個團隊，專注於改進其基礎設施。Jeff Bezos意識到這個內部基礎設施的潛力，可以成為一個革命性的雲端運算平台。在隨後的幾年中，這個團隊努力開發和改進AWS服務，並在2006年正式向公眾推出。AWS的創立使得企業能夠更有效地運行他們的應用程序，並在全球範圍內擁有更大的影響力。'
                ),
                TextSendMessage(
                    text=f'AWS的故事開始於2003年，當時亞馬遜公司的Jeff Bezos和他的團隊認識到他們所擁有的龐大基礎設施可以成為一個有力的雲端運算平台。在幾年的努力和創新後，他們於2006年推出了AWS，這個平台重新定義了企業和開發者如何運行應用程序的方式。而Jeff Bezos的願景是建立一個開放、可靠且可擴展的雲端解決方案，這種精神在AWS的成功中得到了完美的體現。'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/jeff_bezos.jpeg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/jeff_bezos.jpeg",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 提供的業務":
            reply_messages = [
                TextSendMessage(
                    text=f'當然！AWS（Amazon Web Services）提供多樣化的雲端運算服務，包括計算、儲存、資料庫、機器學習、人工智慧、物聯網、區塊鏈等。舉例來說，EC2提供虛擬伺服器，S3提供無限儲存空間，RDS提供受管理的資料庫服務，而AI服務如Lex和Polly則能讓你輕鬆整合語音和自然語言處理功能。AWS致力於為客戶提供完整、可擴展且高度安全的雲端解決方案。'
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

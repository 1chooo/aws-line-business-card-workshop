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
                    text=f'AWS ☁️ 的創辦故事始於 2003 年，當時亞馬遜公司的 Jeff Bezos 意識到他們在建設強大的內部基礎設施方面取得了不錯的進展！'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/jeff_bezos.jpeg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/jeff_bezos.jpeg",
                ),
                TextSendMessage(
                    text=f'他認識到這個基礎設施可以成為一個強大的雲端運算平台，能夠為其他企業提供服務。於是在 2006 年，AWS ☁️ 正式推出，開始提供雲端服務。'
                ),
                TextSendMessage(
                    text=f'AWS ☁️ 的成功與其開放性、靈活性和不斷創新的企業文化有關。'
                ),
                TextSendMessage(
                    text=f'這一切都源於 Jeff Bezos 對技術和未來的敏銳洞察力✨，他能看到潛在的機會並推動公司朝著新的方向發展。'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 提供的業務":
            reply_messages = [
                TextSendMessage(
                    text=f'AWS ☁️ 提供多樣化的雲端運算服務，包括計算（如 EC2 與 Lambda）、儲存（如 S3）、資料庫（如 RDS）、機器學習、人工智慧、物聯網、區塊鏈等。'
                ),
                TextSendMessage(
                    text=f'舉例來說，EC2 提供虛擬伺服器，Lambda 則提供無需管理伺服器的程式碼執行環境。同時，S3 提供無限儲存空間，RDS 提供受管理的資料庫服務。API Gateway 可建立、部署和管理安全的 API，讓您輕鬆構建和監控應用程式介面。'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/aws_services.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/aws_services.png",
                ),
                TextSendMessage(
                    text=f'AWS ☁️ 致力於為客戶提供完整、可擴展且高度安全的雲端解決方案。'
                ),
                TextSendMessage(
                    text=f'且 AWS ☁️ 的多樣性和高度可靠性確保您可以找到符合您業務需求的解決方案。'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 的16項領導力準則":
            reply_messages = [
                TextSendMessage(
                    text=f'AWS ☁️ 的 16 項領導力準則是文化核心價值觀的體現，著重於滿足客戶需求並超越期望，以及追求卓越而非滿足現狀。'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/aws_leadership.jpg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/aws_leadership.jpg",
                ),
                TextSendMessage(
                    text=f'同時，這些準則強調了團隊合作、創新、效率和對變革的開放態度，成為公司文化中的重要支柱。'
                ),
                TextSendMessage(
                    text=f'透過這些準則，AWS ☁️ 激勵著員工發揮最佳表現，持續挑戰自我，並不斷追求個人與團隊的成長。'
                ),
                TextSendMessage(
                    text=f'這些準則不僅是指導方針，更是推動公司進步和持續發展的動力所在。'
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想知道 AWS 未來的發展方向":
            reply_messages = [
                TextSendMessage(
                    text=f'AWS ☁️ 將持續引領雲端運算發展，擴展服務和解決方案以滿足客戶需求。'
                ),
                TextSendMessage(
                    text=f'未來將深入研究人工智慧、機器學習等，提供更智能、靈活的解決方案。'
                ),
                TextSendMessage(
                    text=f'AWS ☁️ 致力於提升雲端基礎設施性能和安全性，保障客戶資料安全。'
                ),
                TextSendMessage(
                    text=f'AWS ☁️ 積極推動環保和可持續發展，尋求綠色能源方案與客戶攜手實現可持續目標'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/aws_future.jpg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/aws_future.jpg",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想了解 AWS LINE BOT 開發團隊":
            reply_messages = [
                TextSendMessage(
                    text=f'嗨！👋 \n我們是第五屆 AWS Educate 校園大使'
                ),
                TextSendMessage(
                    text=f'我是你的 AWS 小幫手，將帶你探索 Amazon Web Services 的無限可能。'
                ),
                TextSendMessage(
                    text=f'將陪你一同踏上雲端運算的冒險之旅。AWS 提供豐富多元的雲端服務，從運算到儲存，應有盡有。'
                ),
                TextSendMessage(
                    text=f'我會與你分享 AWS 的最新動態、技術見解，以及 AWS Educate 獨家的學習體驗，讓我們一同迎接科技的挑戰吧！🌟💡'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/aws_educate.png",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/aws_educate.png",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        elif event_text == "我想了解如何成為 AWS Educate 校園大使":
            reply_messages = [
                TextSendMessage(
                    text=f'成為AWS Educate校園大使是一個很讚的機會👍 '
                ),
                TextSendMessage(
                    text=f'你可以積極參與AWS Educate舉辦的大小活動，確保你充分了解AWS雲端運算和相關技術。\n也可以先透過以下連結註冊體驗 AWS Educate\n👉🏻 https://awseducate.tw/2'
                ),
                TextSendMessage(
                    text=f'如果你有興趣成為AWS Educate校園大使，建議你可以定期關注AWS Educate的社群與活動內容，以便瞭解校園大使計劃的最新消息。'
                ),
                TextSendMessage(
                    text=f'期待你能加入 AWS Educate 校園大使，讓我們一起過程中都能有所收穫 🫵🏻'
                ),
                ImageSendMessage(
                    original_content_url = "https://line-workshop-test.s3.amazonaws.com/become_ambassader.jpg",
                    preview_image_url = "https://line-workshop-test.s3.amazonaws.com/become_ambassader.jpg",
                ),
            ]
                
            line_bot_api.reply_message(
                event.reply_token,
                reply_messages
            )
        else:
            reply_messages = [
                TextSendMessage(
                    text=f'不好意思！我們現在還不認識這句話，或許可以試試點擊選單內容！'
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

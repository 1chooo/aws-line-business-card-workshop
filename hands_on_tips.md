# 2023/12/08 AWS LINE Business Card Workshop Hands-On Tips

為公司打造公關形象，打造 line bot 推播公司的資訊。

## Table of Contents
1. 挑選品牌
2. 透過以下主題介紹公司
   - [ ] 設定加入好友訊息
   - [ ] 公司創辦的故事
   - [ ] 公司提供業務
   - [ ] 公司的技術背景
   - [ ] 公司的宗旨
   - [ ] 公司的未來展望
   - [ ] 製作 LINE BOT 的開發團隊
3. 建立 line bot
4. 將 line bot 加入 AWS 雲服務

## 挑選品牌
請透過以下與 AWS 有關的品牌，挑選一個你喜歡的品牌，並且會是今天主要推播的品牌。（又或是還有其他興趣並且同樣有使用 AWS 服務的品牌）


![](./imgs/brands.png)

#### ☁️ 以下將會以 `AWS` 為例子 ☁️

## 透過以下主題介紹公司

可以透過以下主題來讓使用者了解公司的資訊，並且可以適時地透過照片的輔助來讓使用者更加了解公司的資訊。

1. 公司創辦的故事
2. 公司提供業務
3. 公司的技術背景
4. 公司的宗旨
5. 公司的未來展望
6. 製作 LINE BOT 的開發團隊

並且可以下載此 Excel 模板 [replying_example.xlsx](./replying_example.xlsx) 來進行編輯，以儲存討論的成果。

### 設定加入好友訊息

| 回覆 1 | 回覆 2 | 回覆 3 | 回覆 4 | 回覆 5 |
|:-:|:-:|:-:|:-:|:-:|
| Hi | HiHi | HiHiHi | HiHiHiHi | |

### 公司創辦的故事

| LINE BOT 關鍵字 | 回覆 1 | 回覆 2 | 回覆 3 | 回覆 4 | 回覆 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 我想知道 AWS 創辦故事 | 我想知道 AWS 創辦故事 1 | 我想知道 AWS 創辦故事 2 | 我想知道 AWS 創辦故事 3 | 我想知道 AWS 創辦故事 4 | https://line-workshop-test.s3.amazonaws.com/01_story.png |

```python
elif event_text == "你們的關鍵字":
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
```

### 公司提供業務

| LINE BOT 關鍵字 | 回覆 1 | 回覆 2 | 回覆 3 | 回覆 4 | 回覆 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 我想知道 AWS 提供的業務 | 我想知道 AWS 提供的業務 1 | 我想知道 AWS 提供的業務 2 | 我想知道 AWS 提供的業務 3 | 我想知道 AWS 提供的業務 4 | https://line-workshop-test.s3.amazonaws.com/02_business.png |

```python
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
```

### 公司的技術背景

| LINE BOT 關鍵字 | 回覆 1 | 回覆 2 | 回覆 3 | 回覆 4 | 回覆 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 我想知道 AWS 技術背景 | 我想知道 AWS 技術背景 1 | 我想知道 AWS 技術背景 2 | 我想知道 AWS 技術背景 3 | 我想知道 AWS 技術背景 4 | https://line-workshop-test.s3.amazonaws.com/03_tech.png |

```python
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
```

### 公司的宗旨

| LINE BOT 關鍵字 | 回覆 1 | 回覆 2 | 回覆 3 | 回覆 4 | 回覆 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 我想知道 AWS 的領導力準則 | 我想知道 AWS 的領導力準則 1 | 我想知道 AWS 的領導力準則 2 | 我想知道 AWS 的領導力準則 3 | 我想知道 AWS 的領導力準則 4 | https://line-workshop-test.s3.amazonaws.com/04_leadership.png |

```python
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
```

### 公司的未來展望

| LINE BOT 關鍵字 | 回覆 1 | 回覆 2 | 回覆 3 | 回覆 4 | 回覆 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 我想知道 AWS 未來的發展方向 | 我想知道 AWS 未來的發展方向 1 | 我想知道 AWS 未來的發展方向 2 | 我想知道 AWS 未來的發展方向 3 | 我想知道 AWS 未來的發展方向 4 | https://line-workshop-test.s3.amazonaws.com/05_future.png |

```python
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
```

### 製作 LINE BOT 的開發團隊

| LINE BOT 關鍵字 | 回覆 1 | 回覆 2 | 回覆 3 | 回覆 4 | 回覆 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 我想了解 AWS LINE BOT 開發團隊 | 我想了解 AWS LINE BOT 開發團隊 1 | 我想了解 AWS LINE BOT 開發團隊 2 | 我想了解 AWS LINE BOT 開發團隊 3 | 我想了解 AWS LINE BOT 開發團隊 4 | https://line-workshop-test.s3.amazonaws.com/06_developing.png |

```python
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
```

## 將 line bot 加入 AWS 雲服務
### Services
- [API Gateway](https://aws.amazon.com/tw/api-gateway/)：用來溝通Line和Lambda
- [Lambda](https://aws.amazon.com/tw/lambda/)：用來傳送名片訊息
- [S3](https://aws.amazon.com/tw/s3/)：用來儲存檔案 ex: image or txt

### 架構
- webhook：一種即時通知的機制，會在特定情況下觸發，呼叫一串叫做API的網址。在本次工作坊是Line Bot收到任何訊息的情況下，之後呼叫剛剛說的API。
- API：是一個允許應用程式之間通訊的橋樑，負責傳送和回應訊息。在本次工作坊會由Webhook呼叫，並將Line收到的訊息傳送給Lambda處理。
- Lambda：一個只用於執行程式的伺服器，會在事件發生時執行我們設定的函式Function。在本次工作坊的事件是API被呼叫的時候，會執行發送名片訊息的程式，回傳給LINE。

### Create Lambda Function
Enter Lambda Console:  
1. Choose **[Functions](https://console.aws.amazon.com/lambda/home#/functions)**
2. Click **Creates fcunction**
3. Type **Function name** whatever you want
4. Select **Python 3.9**
5. Click Create function

### Edit your Lambda Function
After you create Lambda Function successfully, you need to paste you code.  
1. Scroll down and paset your code in code source.
2. Click **Test**
3. Customize your **Event name**
4. Click **Save**
5. Click **Deploy**
6. After successful deployment, click **Test**  
You will see some errors because we lost some libraries.
To inform Lambda about the required modules, we need to upload the .zip file to the layer.

### Upload .zip to Layer
1. Open **Menu**
2. Click **Layers**
3. Click **Create layer**
4. Type **Name** and  download the [line-bot-sdk.zip](https://raw.githubusercontent.com/1chooo/aws-line-business-card/main/line-bot-sdk.zip) to upload to layer
   , Choose **x86_64**
   , Select **Python 3.9**
5. Click **Create**

### Add Layer to your Function
Back to your Lambda Function and scroll down to find the Layers
1. Click **Add a layer** from Layers
2. Select **Custom layers**
3. Choose the layer you just created
4. Click **Add**  
After layer is added, you can try Test again, but it will pop new error.
Because the lambda can't find the **Line Bot KEY**, so we need to add **Environment variables**

### Add Environment variables
1. **Configuration**
2. **Environment variables**
3. **Edit**
4. Click **Add Environment variable** two times, and input **CHANNEL_ACCESS_TOKEN** and **CHANNEL_SECRET** seperately  
Now, we need to go back to the [Line Developers console](https://developers.line.biz/console/) to obtain the these two KEY.
Choose your Line Bot just created, and find the CHANNEL_ACCESS_TOKEN in **Messaging API** and CHANNEL_SECRET in **Basic settings**  
5. Select **Messaging API** and scroll to the bottom. Issue the **Channel access token** and copy this to the **CHANNEL_ACCESS_TOKEN**
6. Select **Basic settings** and scroll to the bottom. Copy **Channel secret** to the **CHANNEL_SECRET**
7. Back to Lambda and **Save**  
You can test again, but you will encounter another error. This is because the request is not originating from Line. When making requests to this program, we check whether the message is coming from Line to avoid malicious requests.
So, now we need to use API Gateway to create an API that receives the correct requests from Line.

### Create API
Enter **[API Gateway](https://console.aws.amazon.com/apigateway)** Console:  
1. Find the **REST API** and click **Build**
2. Customize your **API name** and click **Create API**
3. Click **Create method** in Methods
4. Select Method type with **POST**
5. Switch on the **Lambda proxy integration**
6. Choose your **Lambda Function**
7. **Create method**
8. Click **Deploy API**
9. Select **New stage** and type **prod** to stage name
10. Deploy
11. After API is deployed, copy the **Invoke URL**  
This URL is the Webhook URL, so we need to paste it into the Line Bot settings.

### Webhook Settings
Go to Line Developers Console and choose your Line Bot's Messeging API  
1. Scroll down to find the **Webhook settings**, and click **Edit** to paste the **Invoke URL**
2. Switch on **Use webhook**
3. Click **Verify** and check for **Success**

## CONTACT INFO.

> AWS Educate Cloud Ambassador, Technical Support </br>
> **Hugo ChunHo Lin**
> 
> <aside>
>   📩 E-mail: <a href="mailto:hugo970217@gmail.com">hugo970217@gmail.com</a>
> <br>
>   🧳 Linkedin: <a href="https://www.linkedin.com/in/1chooo/">Hugo ChunHo Lin</a>
> <br>
>   👨🏻‍💻 GitHub: <a href="https://github.com/1chooo">1chooo</a>
>    
> </aside>

## License
Released under [MIT](./LICENSE) by [AWS Educate TW](https://aws.amazon.com/tw/education/awseducate/), [Hugo ChunHo Lin](https://github.com/1chooo).

This software can be modified and reused without restriction.
The original license must be included with any copies of this software.
If a significant portion of the source code is used, please provide a link back to this repository.

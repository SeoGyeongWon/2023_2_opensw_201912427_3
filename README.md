# 2023_2_opensw_201912427_3

3.텔레그램 봇 + ChatGPT 연동

<img width="960" alt="연동" src="https://github.com/SeoGyeongWon/2023_2_opensw_201912427_3/assets/126853734/8fd05a4f-5093-4e92-ab73-ab3798ffe06e">
<br/>
<br/>
<br/>

소스코드<br/><br/><br/><br/>

import telegram <br/>
import asyncio <br/>
import openai <br/><br/>

openai.api_key = "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" <br/> <br/>

async def main(): <br/>
    # OpenAI GPT-3.5 Turbo로 메시지 생성 <br/>
    completion = openai.ChatCompletion.create( <br/>
        model="gpt-3.5-turbo", <br/>
        messages=[ <br/>
            {"role": "system", "content": "You are the smartest assistant, skilled in explaining complex programming concepts with creative flair."}, <br/>
            {"role": "user", "content": "경기대학교에 관해 5문장으로 정리해줘"} <br/>
        ], <br/>
    ) <br/> 

    gpt_response = completion['choices'][0]['message']['content'] <br/><br/><br/>


    token = "6898150295:AAE8hxjfg3rQuGPzuEuwHPLNExqlZ3yAWKs" <br/>
    bot = telegram.Bot(token=token) <br/>
    chat_id = "6905523486"   <br/>

    await bot.send_message(chat_id=chat_id, text=gpt_response) <br/>

if __name__ == "__main__": <br/>
    if hasattr(asyncio, "run"): <br/>
        asyncio.run(main()) <br/>
    else: <br/>
        loop = asyncio.get_event_loop() <br/>
        loop.run_until_complete(main()) <br/>

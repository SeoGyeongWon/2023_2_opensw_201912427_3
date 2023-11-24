import telegram
import asyncio
import openai

openai.api_key = "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"

async def main():
    # OpenAI GPT-3.5 Turbo로 메시지 생성
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the smartest assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "경기대학교에 관해 5문장으로 정리해줘"}
        ],
    )

    gpt_response = completion['choices'][0]['message']['content']


    token = "6898150295:AAE8hxjfg3rQuGPzuEuwHPLNExqlZ3yAWKs"
    bot = telegram.Bot(token=token)
    chat_id = "6905523486"  

    await bot.send_message(chat_id=chat_id, text=gpt_response)

if __name__ == "__main__":
    if hasattr(asyncio, "run"):
        asyncio.run(main())
    else:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
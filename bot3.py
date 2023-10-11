import telegram
import asyncio
bot = telegram.Bot(token="6490343462:AAGLtHVEHDhdXV4QCs_IhgZqAa0qNP76BOY")
chat_id = '-4069828355'
text = 'Message'
async def main():
    await bot.send_message(chat_id=chat_id, text=text)
asyncio.run(main())
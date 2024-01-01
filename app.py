from telegram import Bot, InputMediaPhoto
from telegram.error import TelegramError
import asyncio

# Thay thế 'YOUR_BOT_TOKEN' bằng token của bot bạn
bot_token = '6175232239:AAHJ9fyetFQuqVtvlz7vpoezJZvQrXWYYe4'
chat_id = '-1002110020789'  # Thay thế 'TARGET_CHAT_ID' bằng ID của cuộc trò chuyện bạn muốn gửi tin nhắn đến

async def send_image_to_telegram(token, chat_ids, image_path, texts):
    try:
        bot = Bot(token=token)

        for chat_id, text in zip(chat_ids, texts):
            caption = text
            await bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'), caption=caption, parse_mode='HTML')

    except TelegramError as e:
        print(f"Error sending image and text: {e}")


def main():
    message = "🔔 Dự đoán kế tiếp: <b>Bàn1: NHÀ CÁI</b>🔔 Tổng lãi:"
    asyncio.run(send_image_to_telegram(token=bot_token, chat_ids=[chat_id], image_path="zone_result_profile1.png", texts=[message]))

if __name__ == "__main__":
    main()

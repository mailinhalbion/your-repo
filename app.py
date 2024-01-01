from telegram import Bot

# Thay thế 'YOUR_BOT_TOKEN' bằng token của bot bạn
bot_token = '6175232239:AAHJ9fyetFQuqVtvlz7vpoezJZvQrXWYYe4'
chat_id = '-1002110020789'  # Thay thế 'TARGET_CHAT_ID' bằng ID của cuộc trò chuyện bạn muốn gửi tin nhắn đến

def send_message(message):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# Gọi hàm để gửi tin nhắn
send_message("Xin chào, đây là tin nhắn tự động từ bot Telegram!")

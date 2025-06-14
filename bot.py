import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = list(map(int, os.getenv("ADMINS", "").split(",")))
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

WELCOME_TEXT = """سلام 👋
به ربات رسمی کاوان دکو خوش اومدی 🌟

برای استفاده از امکانات ربات، لطفاً اول در کانال عضو شو:
📢 https://t.me/{}""".format(CHANNEL_USERNAME)

ABOUT_TEXT = """
🎉 به دنیای کاوان دکو خوش اومدی!

اینجا، هر تکه از چوب، هر رنگ، و هر پیچ‌و‌مهره‌ای قراره بخشی از خونه‌ای بشه که تو با سلیقه‌ات ساختیش.

🧩 ما در کاوان دکو محصولات خلاقانه و دست‌ساز برای دکوراسیون منزل طراحی و تولید می‌کنیم — با یه فرق مهم:
تو انتخاب می‌کنی چه رنگ، چه طرح و چه حس‌وحالی داشته باشن!

🔧 محصولاتمون به صورت قطعه‌ای برات ارسال می‌شن،
با راهنمای مونتاژ ساده‌ای که خودت با یه فنجون قهوه و کمی وقت، می‌تونی کنار هم بذاری‌شون!

🎨 همه چی قابل شخصی‌سازیه:
از رنگ چوب گرفته تا سبک کار — چون ما معتقدیم هر خونه باید امضای صاحبش رو داشته باشه.

📬 اگه سوالی داشتی، یا می‌خوای سفارشت رو ثبت کنی، فقط کافیه بهمون پیام بدی.

🌟
کاوان دکو، دکوراتیو با امضای تو.
"""

CONTACT_TEXT = """
📞 برای ارتباط با ما می‌تونی از راه زیر استفاده کنی:

شماره تماس: 09153446447  
یا همین‌جا بهمون پیام بده!
"""

SOCIALS_TEXT = """
🌐 لینک‌های ما:

📸 اینستاگرام: https://instagram.com/kavandeco  
▶️ یوتیوب: https://youtube.com/@kavandeco
"""

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if not message.chat.type == 'private':
        return
    await message.answer(WELCOME_TEXT, reply_markup=main_menu())

@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await message.answer(ABOUT_TEXT)

@dp.message_handler(commands=['contact'])
async def contact(message: types.Message):
    await message.answer(CONTACT_TEXT)

@dp.message_handler(commands=['links'])
async def socials(message: types.Message):
    await message.answer(SOCIALS_TEXT)

@dp.message_handler()
async def forward_to_admins(message: types.Message):
    for admin in ADMINS:
        await bot.send_message(admin, f"📩 پیام جدید از {message.from_user.full_name}:\n\n{message.text}")
    await message.reply("پیام شما به تیم پشتیبانی ارسال شد ✅")

def main_menu():
    buttons = [
        [types.KeyboardButton("📖 درباره ما")],
        [types.KeyboardButton("📞 ارتباط با ما")],
        [types.KeyboardButton("🌐 لینک‌ها")]
    ]
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(*[btn[0] for btn in buttons])
    return kb

@dp.message_handler(lambda m: m.text == "📖 درباره ما")
async def handle_about(m: types.Message):
    await about(m)

@dp.message_handler(lambda m: m.text == "📞 ارتباط با ما")
async def handle_contact(m: types.Message):
    await contact(m)

@dp.message_handler(lambda m: m.text == "🌐 لینک‌ها")
async def handle_links(m: types.Message):
    await socials(m)

if name == '__main__':
    executor.start_polling(dp, skip_updates=True)
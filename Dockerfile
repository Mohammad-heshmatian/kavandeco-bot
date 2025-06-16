# استفاده از تصویر رسمی پایتون (نسخه پایدارتر، نه 3.13 که هنوز ناسازگاری‌هایی داره)
FROM python:3.11-slim

# تنظیم پوشه‌ی کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل‌های پروژه به داخل کانتینر
COPY . .

# نصب پیش‌نیازها
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# دستور اجرای بات
CMD ["python", "bot.py"]

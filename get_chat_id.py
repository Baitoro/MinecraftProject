import requests

TOKEN = os.getenv("TELEGRAM_TOKEN")

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

data = requests.get(url).json()

print(data)
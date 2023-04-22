import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "4682685")

API_HASH = os.environ.get("API_HASH", "3eba5d471162181b8a3f7f5c0a23c307")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5484278199:AAFui1dWdQOo2L9WL8s75RhcYOi0oSJY5CE") 

FORCE_SUB = os.environ.get("FORCE_SUB", "movie_time_botonly") 

DB_NAME = os.environ.get("DB_NAME","telegramfilesrename")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://filetwo:link@cluster0.o7fziur.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/390208792e429dab23ab3.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '945284066').split()]

PORT = os.environ.get("PORT", "8080")

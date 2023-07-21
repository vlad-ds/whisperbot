import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from fs import get_connector
from oa import transcribe_whisper

load_dotenv()
TOKEN = os.environ["BOT_TOKEN"]
PASSWORD = os.environ["BOT_PWD"]
S3_BUCKET_NAME = os.environ["S3_BUCKET_NAME"]
STORAGE = os.environ["STORAGE"]
AUTHORIZED_CHATS_FILE = "whisperbot/authorized_chats.json"

AUTHORIZED_CHATS_FILE = "whisperbot/authorized_chats.json"

# get the file connector and load the data
connector = get_connector(STORAGE, S3_BUCKET_NAME)
authorized_chats = connector.read(AUTHORIZED_CHATS_FILE) or []


def start_polling():
    # Create the Application and pass it the token
    application = Application.builder().token(TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("password", password))

    # on voice message transcribe and translate
    application.add_handler(MessageHandler(filters.VOICE, handle_voice_message))

    # run the bot
    application.run_polling()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'''Welcome!
Use the /password command to authorize this chat. You only have to do it once for each chat.
''')


async def password(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Authorize a chat if the correct password is entered."""
    chat_id = str(update.effective_chat.id)

    # Get the entered password from the message
    entered_password = ' '.join(update.message.text.split()[1:])

    if entered_password == PASSWORD:
        # If the password is correct, add the chat to the list of authorized chats
        authorized_chats.append(chat_id)
        connector.write(AUTHORIZED_CHATS_FILE, authorized_chats)
        await update.message.reply_text("Success! This chat is now authorized to use the bot.")
    else:
        await update.message.reply_text("Incorrect password.")


async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle a voice message by converting speech to text with the Whisper API and translating it."""
    chat_id = str(update.effective_chat.id)

    if chat_id not in authorized_chats:
        await update.message.reply_text("Chat not authorized yet. Use the /password command to authorize.")
        return

    voice = update.message.voice
    voice_file = await voice.get_file()

    if not os.path.exists("voice_messages"):
        os.makedirs("voice_messages")

    voice_file_path = f"voice_messages/{voice_file.file_id}.oga"
    await voice_file.download_to_drive(custom_path=voice_file_path)
    transcript = transcribe_whisper(voice_file_path)
    os.remove(voice_file_path)
    await update.message.reply_markdown(transcript, reply_to_message_id=update.message.message_id)


def main():
    start_polling()


if __name__ == "__main__":
    main()

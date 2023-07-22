# WhisperBot

WhisperBot is a simple Telegram wrapper over OpenAI's [Whisper](https://openai.com/research/whisper) model. 

Send voice messages to WhisperBot and it will transcribe them for you. It works really well.

WhisperBot uses the `transcribe` endpoint. Whisper will identify the language of your voice message
and transcribe it accurately into that language.

Use cases:

* Dictate emails and documents on the go
* Send voice messages to people who don't speak your language
* Transcribe people's voice messages
* Transcribe any audio by sharing it with WhisperBot
* Not just English: Whisper can transcribe in many languages

Currently, WhisperBot is not available publicly. You can deploy your own instance of the bot and use it with your friends.

## Setup
Use the BotFather to create your bot and save the secret bot token. You can follow the instructions [here](https://core.telegram.org/bots/tutorial).

Sign up for OpenAI and get your API key. 

Clone or fork this repo. Run `pip install -r requirements.txt` to install the dependencies.

Create a `.env` file in the `bin/` directory. Add the following lines:
```commandline
OPENAI_API_KEY=<your OpenAI key>
BOT_TOKEN=<your secret bot token from BotFather>
BOT_PWD=<the password that users will use to authorize chats>
S3_BUCKET_NAME=<the name of your S3 bucket (only if you use S3 as storage)>
STORAGE=<currently can be either s3 or local>
```

Run `python bin/bot.py` to start the bot. That's it! 

# How can I deploy the bot?

See my short guide [here](https://gist.github.com/vlad-ds/b098af8260d57a4490efed68bae50a78).
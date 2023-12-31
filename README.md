# WhisperBot

WhisperBot is a simple Telegram wrapper over OpenAI's [Whisper](https://openai.com/research/whisper) model. 

Send voice messages to WhisperBot and it will transcribe them for you. It works really well.

WhisperBot can use two modes:

* The `transcribe` endpoint, which accurately transcribes the message in its original language. 
* The `translate` endpoint, which translates the message to English regardless of the language.

Use `/mode transcribe` or `/mode translate` to switch between the two modes.

Whisper will identify the language of your voice message
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

## Usage
The first time you use the bot, you need to authorize the chat. Write `/password` followed by the password you set in `.env`. 

If you want other users to use the bot, you can share the password with them. 

You can also add your bot to grup chats and have it translate voice messages there. You need to authorize this in your bot's settings. Go to BotFather on Telegram and write /mybots. Select your bot and then "Bot Settings". Allow Groups and turn Group Privacy off.  

## Storage
WhisperBot remembers which chats are authorized and the mode for each chat. 
This information is stored in a simple JSON file. The STORAGE variable in `.env` determines where this file is stored.
Currently it can be either `local` or `s3`. If you choose `s3`, you need to provide the name of your S3 bucket in `.env`.

## How can I deploy the bot?

See my short guide [here](https://gist.github.com/vlad-ds/b098af8260d57a4490efed68bae50a78).

## Liabilities
* You will incur some cost for using the Whisper API. You can set a monthly budget in your OpenAI account.
* Do not operate the bot without a password as it will allow anyone to indirectly use your OpenAI API key.
* Do not send questionable content to Whisper or you will risk getting your OpenAI API key banned. 
* For the same reason, do not share this bot with people you don't trust.
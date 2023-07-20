# WhisperBot

This is a Telegram bot interface for OpenAI's [Whisper](https://openai.com/research/whisper) model. 

Send voice messages to WhisperBot and it will transcribe them for you. 
The quality is really good!

* Dictate emails and documents on the go
* Send voice messages to people who don't speak your language
* Transcribe any audio by simply sharing it on Telegram
* Transcribe people's voice messages

You will need to setup the bot and host it yourself. Fortunately, it's not too difficult.

## Setup
Use the BotFather to create your bot and save the secret bot token. You can follow the instructions [here](https://core.telegram.org/bots/tutorial).

Sign up for OpenAI and get your API key. 

**Warning: Don't share your bot token or OpenAI API key with anyone!**

Clone or fork this repo. Run `pip install -r requirements.txt` to install the dependencies.

Create a `.env` file in the `bin/` directory. Add the following lines:
```commandline
OPENAI_API_KEY=
BOT_TOKEN=
BOT_PWD=
S3_BUCKET_NAME=
STORAGE=
```

Add your secrets to this file. `BOT_PWD` is a secret password that will allow your users to use the bot.

Currently, STORAGE can be either `s3` or `local`. If you use `s3`, you will need to set up an S3 bucket.

Run `python bin/bot.py` to start the bot. 

That's it! You should now be able to use the bot.

# Remote setup (AWS EC2)
If you run the bot locally, it will stop working when you close the terminal. The alternative is
to host the bot somewhere. 

There are many ways to do this. I chose AWS EC2 as it's a cheap and easy option.

Create an AWS account and start an EC2 instance. Install pip, git and github cli. If you use 
an Amazon Linux image (which is what the free tier offers) you can run the commands in `ec2_start.sh` in this repo.

Connect to your GitHub account with `gh auth login` and clone this repo. Create the `.env` 
in the `bin/` folder and add your secrets.

You should now be able to run the bot with `python whisperbot/bin/bot.py`.

You can use `screen` to run the bot even after you close the connection. See the section below.

I recommend using the `s3` storage option if you are going to run the bot in EC2.

# Use screen to run the bot

`screen` is a tool that allows you to run a process in the background. 
You can use it to run the bot on a remote server.

Use these commands to run screen:

```commandline
# create dedicated session
screen -S whisper

# start the bot
python3 whisperbot/bin/bot.py

# press ctrl+a then d to detach

# list sessions
screen -ls

# return to the session
screen -r whisper

# kill the session
screen -X -S whisper quit
```
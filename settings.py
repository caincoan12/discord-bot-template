import os

# The prefix that will be used to parse commands.
# It doesn't have to be a single character!
COMMAND_PREFIX = ">n"

# The bot token. Keep this secret!
BOT_TOKEN = "NzcwODUxNTI2Mzk4MTgxMzk2.X5jlbQ.FFJp9wHKkY3jPTcQe5TrcFIP E"

# The now playing game. Set this to anything false-y ("", None) to disable it
NOW_PLAYING = COMMAND_PREFIX + "commands"

# Base directory. Feel free to use it if you want.
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

from pocketsphinx import LiveSpeech
from functools import partial
from itertools import chain
import commands

COMMANDS = {
        "lock": commands.lock,
        "play": commands.play,
        "pause": commands.pause,
        "stop": commands.stop,
        "next": commands.next,
        "previous": commands.previous,
        }

def getCommands(speech, keyword):
    words = chain.from_iterable(str(phrase).split() for phrase in speech)
    for word in words:
        if word == keyword:
            yield next(words)

keyword = "apex"
speech = LiveSpeech(dict="kws.dict")
for command in getCommands(speech, keyword):
    f = COMMANDS[command]
    if f:
        f()
    else:
        print(command, "not implemented")

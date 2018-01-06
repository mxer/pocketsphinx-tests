from pocketsphinx import LiveSpeech
from subprocess import call

speech = LiveSpeech(dict='screenlock.dict')
for phrase in speech:
    seg = phrase.segments()
    if 'lock' in seg and 'screen' in seg:
        call("slock")

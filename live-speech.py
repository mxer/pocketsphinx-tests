from pocketsphinx import LiveSpeech

speech = LiveSpeech(dict='simple.dict')
for phrase in speech:
    print(phrase.hypothesis())

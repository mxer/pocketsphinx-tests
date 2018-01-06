# Pocketsphinx Tests

Run these with `python3 <scriptname>.py`; they probably won't work with
Python 2. `pocketsphinx-python` is required. Install it with `pip3 install
pocketsphinx`.

`pocketsphinx-python` depends on PocketSphinx (duh) and PulseAudio. On
Debian, the packages `libpocketsphinx-dev` and `libpulse-dev` should be
installed before pip installation.

## Dictionary files

There are several `.dict` files in this repo. They specify valid mappings from sounds to words. The reason I've used basically one per script is because I've not been able to find a British English phonetic dictionary. Hence, I've been copying words from pocketsphinx's [built-in US dictionary][cmudict] and changing them as appropriate.

[cmudict]: https://raw.githubusercontent.com/cmusphinx/pocketsphinx/master/model/en-us/cmudict-en-us.dict

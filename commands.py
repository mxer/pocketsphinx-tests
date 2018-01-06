# Commands for keyword-start.py
from mpd import MPDClient
from mpd import ConnectionError as MPDConnectionError
from subprocess import call
from contextlib import contextmanager

@contextmanager
def _mpd():
    try:
        mpd = MPDClient()
        mpd.connect("localhost", 6600)
        yield mpd
    finally:
        mpd.close()
        mpd.disconnect()

def lock():
    call("slock")

def play():
    with _mpd() as mpd:
        mpd.play()

def pause():
    with _mpd() as mpd:
        mpd.pause()

def stop():
    with _mpd() as mpd:
        mpd.stop()

def next():
    with _mpd() as mpd:
        mpd.next()

def previous():
    with _mpd() as mpd:
        mpd.previous()

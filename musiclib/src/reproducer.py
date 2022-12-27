from threading import Thread
import sounddevice as sd
import soundfile as sf

def play_audio(filePath):
    print("Going to play audio {0}...".format(filePath))
    data, fs = sf.read(file=filePath, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()


def reproduce_audio(audioFilePath: str):
    reproducer_thread = Thread(target=play_audio, args=(audioFilePath,))
    reproducer_thread.run()
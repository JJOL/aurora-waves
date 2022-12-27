from reproducer import reproduce_audio
import os

if __name__ == "__main__":
    print("Starting music analysis...")
    wavfile = os.path.join(os.getcwd(), 'disco.00000.wav')
    print(wavfile)
    reproduce_audio(wavfile)
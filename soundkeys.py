import pyaudio
import numpy as np

class pianoSound:
    def __init__(self, freq):
        self.freq = freq

    def play_sound(self):
        p = pyaudio.PyAudio()
        fs = 1000       # sampling rate, Hz, must be integer
        duration = 1.5   # in seconds, may be float

        # generate samples, convert to float32 array
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*self.freq/fs))
        samples = samples.astype(np.float32)

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32, 
                channels=1, rate=fs, output=True)

        # play sound
        stream.write(samples)
        stream.stop_stream()
        stream.close()
        p.terminate()

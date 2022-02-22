import synthesizer
from synthesizer import Player, Synthesizer, Waveform
import numpy as np
import time
import pyaudio

BITRATE = 44100     #number of frames per second/frameset.  
CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SAMPLE_LENGTH = 5

# open audio device
py_audio = pyaudio.PyAudio()

# generate audio
synthesizer = Synthesizer(osc1_waveform=Waveform.square, osc1_volume=0.2, use_osc2=False, rate=BITRATE)
out_wave = synthesizer.generate_constant_wave(440.0, SAMPLE_LENGTH)

def stream_callback(wave, frame):
    audio_data = (wave * float(2 ** 15 - 1)).astype(np.int16).tobytes()
    index = 0

    def callback(in_data, frame_count, time_info, status):
        nonlocal audio_data
        nonlocal index
        nonlocal frame
        print("got data!")
        frame.append(in_data)
        data_length = frame_count * CHANNELS * 2
        data = audio_data[index:(index+data_length)]
        index += data_length

        return (data, pyaudio.paContinue)

    return callback


frame_data = []


stream_options = {
    "format": FORMAT,
    "channels": CHANNELS,
    "rate": BITRATE,
    "output": True,
    "stream_callback": stream_callback(out_wave, frame_data)
}

# Open Streams
stream_out = py_audio.open(**stream_options)

stream_out.start_stream()

# wait for stream to finish (5)


print("Done!")


stream_out.stop_stream()
stream_out.close()


py_audio.terminate()
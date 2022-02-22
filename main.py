import pyaudio
import numpy as np
import multiprocessing
import time



volume = 0.2     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 0.1   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array


# for paFloat32 sample values must be in range [-1.0, 1.0]

def run(queue):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
    
    stream.start_stream()
    
    try:
        while(True):
            samples = queue.get()
            stream.write(samples)
            
    except:
        pass
    finally:
        print('CLOSE STREAM')
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        
queue = multiprocessing.Queue()
proc_play_music = multiprocessing.Process(
    target=run, args=(queue,))
proc_play_music.start()


start = 0
last_write = time.time()
for i in range(1000):
    print('START:', time.time())
    samples = (np.sin(2*np.pi*np.arange(
        start, start + fs*duration)*f/fs)).astype(np.float32)

    print(len(samples))
    start += fs*duration
    wait_time = 1 - (time.time() - last_write)
        
    queue.put(volume*samples)
    last_write = time.time()





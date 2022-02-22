from abc import ABC, abstractmethod
import numpy as np
import time

import usb.core
import time
import multiprocessing
import pyaudio


from core.session import *
from const.all import *

class InputMidiRoland():
    
    def __init__(self):
        self.device = usb.core.find(idVendor=0x0582, idProduct=0x0156)
        self.endpoint = self.device[0].interfaces()[0].endpoints()[1]
        i = self.device[0].interfaces()[0].bInterfaceNumber
        self.device.reset()

        if self.device.is_kernel_driver_active(i):
            self.device.detach_kernel_driver(i)

        self.device.set_configuration()
        

    def event_handler(self, record):
        "TODO: Add more feature"
        if len(record) > 0:
            if record[0] == 9:
                print('PUSH_BUTTON')
            if record[0] == 8:
                print('UNPUSH_BUTTON')
            if record[0] == 14:
                print('CHANGE_TREMOLO')
            if record[0] == 11 and record[2] == 71:
                print('CHANGE_C2')
            if record[0] == 11 and record[2] == 74:
                print('CHANGE_C1')
            if record[0] == 12:
                print('PUSH_S')
           
            
        return
        
    def run(self, queue):
        while(True):
            r = self.device.read(
                self.endpoint.bEndpointAddress,
                self.endpoint.wMaxPacketSize, 100000)
            queue.put(r)
    

session = Session()


"INIT roland controller"
input_midi_roland = InputMidiRoland()

queue = multiprocessing.Queue()
proc_scan_midi_port = multiprocessing.Process(
    target=input_midi_roland.run, args=(queue,))
proc_scan_midi_port.start()

input_node = InputNodeMidi(session, queue)

button_midi_2_freq = ButtonMidi2Freq(session)

session.add_link(
    Link(session,
         input_node.out_fields['buttons_pushed'],
         button_midi_2_freq.fields['buttons_pushed']
    )
)

sqr_node = SqrNode(session)

session.add_link(
    Link(session,
         button_midi_2_freq.out_fields['freq_pushed'],
         sqr_node.fields['freq_pushed']
    )
)

output_node = OutPutNode(session)

session.add_link(
    Link(session,
         sqr_node.out_fields['output'],
         output_node.fields['signal']
    )
)


def run(queue):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=BITRATE,
                    output=True)

    stream.start_stream()

    try:
        while (True):
            samples = queue.get()
            start = time.time()
            stream.write(samples)
            print('PLAY:', time.time() - start)

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

volume = 0.1
for i in range(10000):
    start = time.time()
    output_node.evaluate()
    queue.put(volume*output_node.out_fields['output'].get_value())
    session.stats.append({})
    time.sleep(0.01)

session.write2file()



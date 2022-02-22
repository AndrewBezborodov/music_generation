#!/usr/bin/python
import usb.core
import time
import multiprocessing


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
    

if __name__ == '__main__':            
    input_midi_roland = InputMidiRoland()
    
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(
        target=input_midi_roland.run, args=(queue,))
    p.start()
    
    freq_start2time = {}
    freq_end2time = {}
    freq_push2time = {}
    while(True):
        record = queue.get()
        print('FETCH FROM QUEUE', record)
        if len(record) > 0:
            for i in range(round(len(record) / 4)):
                if record[i*4] == 8:
                    freq_end2time[record[i*4+2]] = time.time()
                    if record[i*4+2] in freq_push2time:
                        freq_push2time.pop(record[i*4+2])
                if record[i] == 9:
                    freq_start2time[record[i*4+2]] = time.time()
                    freq_push2time[record[i*4+2]] = time.time()

            
        print(freq_push2time)
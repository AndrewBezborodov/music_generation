from core.base_element import BaseElement
from core.objects.field import Field

from const.field_constants import *

import time


class InputNodeMidi(BaseElement):
    __name__ = 'InputNodeMidi'
    """
    manage with Queue.
    """
    
    def __init__(self, session, queue):

        super().__init__(session, None)
        self.queue = queue
        self.freq_push2time = {}
        self.fields = {}
        self.out_fields = {
            'buttons_pushed' : Field('buttons_pushed', DICT, {20:2,32:4}, session, self)
        }
    
    def run(self):
        """Wait for 0.001 seconds"""
        try:
            record = self.queue.get(timeout=0.001)
        except:
            record = {}
        
        if len(record) > 0:
            for i in range(round(len(record) / 4)):
                if record[i*4] == 8:
                    if record[i*4+2] in self.freq_push2time:
                        self.freq_push2time.pop(record[i*4+2])
                if record[i*4] == 9:
                    self.freq_push2time[record[i*4+2]] = time.time()
                           
        self.set_out_field_value('buttons_pushed', self.freq_push2time)

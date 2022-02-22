from core.base_element import BaseElement
from core.objects.field import Field

from const.field_constants import *
from const.all import *
from core.utils import *

import numpy as np
import time

class SqrNode(BaseElement):
    __name__ = 'Squere'
    
    def __init__(self, session, offset=0, freq=0):

        super().__init__(session, None)
        
        self.fields = {
            'freq_pushed':   Field('freq_pushed'  ,VECTOR, 0.00001, session, self), 
            'signal': Field('signal'  ,VECTOR, np.arange(BITRATE / FPS), session, self)
        }
        self.out_fields = {
            'output': Field('output', VECTOR, 0, session, self)
        }

    def run(self):
        freq_pushed = self.get_field_value('freq_pushed')
        signal = np.array([self.get_field_value('signal') for freq in freq_pushed]).T
        freq_pushed = np.array([list(freq_pushed.keys())])

        start = time.time()
        #output_2 = (np.sin(2*np.pi*signal*freq_pushed/BITRATE)).astype(np.float32)
        print('TIME FOR CALC', time.time() - start)
        output = 2 * (np.floor_divide(signal, np.round(BITRATE / freq_pushed / 2)) % 2) - 1
        self.set_out_field_value('output',output.T)
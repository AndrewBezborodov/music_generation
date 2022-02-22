from core.base_element import BaseElement
from core.objects.field import Field

from const.all import *
from const.field_constants import *

import pyaudio
import numpy as np
import time

class OutPutNode(BaseElement):
    __name__ = 'OutPutNode'
    
    def __init__(self, session):
        super().__init__(session, None)
        
        self.fields = {
            'signal': Field('signal',VECTOR, np.zeros(BITRATE), session, self)
        }
        self.out_fields = {
            'output': Field('output', VECTOR, 0, session, self)
        }

        
    def run(self, ):
        output = self.fields['signal'].get_value().sum(axis=0).astype(np.float32)
        print(output.shape)
        self.set_out_field_value('output', output)



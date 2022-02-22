from abc import ABC, abstractmethod
import numpy as np
import time


from core.session import *

session = Session() 
BITRATE = 44000

input_node = InputNode(session, 'MIDI')
sqr_node = SqrNode(session)
output_node = OutPutNode(session)

session.add_link(
    Link(session, 
         input_node.out_fields['output'],
         sqr_node.fields['freq']
    )
)

session.add_link(
    Link(session, 
         sqr_node.out_fields['output'],
         output_node.fields['output']
         
    )
)

start = time.time()
output_node.evaluate()
Y = output_node.get_field_value('output')
print(time.time() - start)
print(Y.mean(), Y.std())

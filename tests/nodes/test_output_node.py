from core.session import *
from core.objects.nodes.outputnode import OutPutNode

import unittest

import numpy as np

class TestOutputNode(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.session = Session()
        self.output_node = OutPutNode(self.session)

        super(TestOutputNode, self).__init__(*args, **kwargs)

    def test_run(self):
        # JUST PLAY SOUND
        print('START WRITE')
        volume = 0.2  # range [0.0, 1.0]
        fs = 44100  # sampling rate, Hz, must be integer
        duration = 3  # in seconds, may be float
        f = 440.0
        samples = np.array([(np.sin(2 * np.pi * np.arange(
            44100 * duration) * f / fs)).astype(np.float32)])

        self.output_node.volume = 0.1
        self.output_node.fields['signal'].set_value(samples)
        self.output_node.run()
        print('END WRITE')



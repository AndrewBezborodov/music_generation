from core.session import *
from core.objects.nodes.sqrnode import SqrNode
from const.all import *

import unittest

class TestSqrNode(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        self.session = Session()
        self.sqr_node = SqrNode(self.session)
        
        
        super(TestSqrNode, self).__init__(*args, **kwargs)
        
    def test_run(self):
        self.sqr_node.fields['freq_pushed'].set_value(
            {60: 1645258781.628589, 100: 1645258783.6599674, 120:0}
        )
        self.sqr_node.run()
        data = self.sqr_node.out_fields['output'].get_value()
        self.assertEqual(data.shape, (3,BITRATE))
        
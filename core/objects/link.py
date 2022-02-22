from core.base_element import BaseElement
    
class Link(BaseElement):
    
    def __init__(self, session, element_out,element_in):
        self.element_out=element_out
        self.element_in=element_in
        super().__init__(session, None)
        
    def run(self):
        pass
    
    def __dict__(self):
        return {'type': 'Link', 'element_out': self.element_out.id, 'element_in': self.element_in.id}
     
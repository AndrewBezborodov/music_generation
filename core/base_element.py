from abc import ABC, abstractmethod
import time

class BaseElement(ABC):
    def __init__(self, session, parent):
        self.session = session
        self.id = self.session.add_object(self)
        self.parent = parent
        self.active = True
        self.already_run = False
        
        self.meta = {}


    
    @abstractmethod
    def run(self):
        pass
    
    def get_field_value(self, field):
        return self.fields[field].get_value()
    
    def set_field_value(self, field, value):
        self.fields[field.name].set_value(value)
        
    def get_out_field_value(self, field):
        return self.out_fields[field.name].get_value()
    
    def set_out_field_value(self, field, value):
        self.out_fields[field].set_value(value)
        
    def change_meta(self, source):
        self.meta = source
    
    def evaluate(self):
        start = time.time()
        print(f'RUN {self.__name__}')
        set_of_prev = set()
        for field in self.fields.values():
            out_field = self.session.links.element_in2elements_out.get(field)
            if out_field:
                set_of_prev.add(out_field)
        
        for element in set_of_prev:
            if not element.already_run:
                print('START EVAL - ',element.parent)
                element.parent.evaluate()
                print('END EVAL - ',element.parent)
            else:
                print('Already runnning')
            
        self.run()
        
        print(self.out_fields.get('buttons_pushed'))
        
        print(f'COPY RUN {self.__name__}')
        for field_out in self.out_fields.values():
            for field_in in self.session.links.element_out2element_in_fields.get(field_out, []):
                print(field_in.parent, field_in.name, field_out.parent, field_out.name)
                field_in.parent.set_field_value(field_in, self.get_out_field_value(field_out))
                print('STILL ALIVE')
                
        self.already_run = True
        print(f'END {self.__name__}')
        self.session.stats[-1][self.__name__] = time.time() - start
        
    def __dict__(self):
        return {'id': self.id,'type': 'node', 'name': self.__name__, 
                'meta': self.meta, 
                'fields_in': list(map(lambda x: x.__dict__(), self.fields.values())), 
                'fields_out': list(map(lambda x: x.__dict__(), self.out_fields.values()))}
        
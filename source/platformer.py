{"STACK: MAIN MENU": {
    "EVENT TYPE": {
        EventInstance: [listeners]
        }
    }
}


class EventListener(object):
    _active_stack = None
    _event_stacks = {}
    _event_bindings = {}
    
    def add_stack(self, name):
        _event_stack[name] = {}
    
    def remove_stack(self, name):
        if name in _event_stack:
            #TODO event stack remove
            for event_type in _event_stack:
                pass
    
    def event_listen(self, event):
        
    
    def event_emit(self, event):
        if event.name in _event_bindings

class Event:
    def _respects_pattern_of(self, event):
        """Override this method to, for instance, check for presses of a key"""
        return True

class KeyPress(Event):
    name = "KeyPress"
    def __init__(self, key):
        

class MousePress(Event):
    def __init__(self, button):
        


class Windowing:
    def __init__(self):
        pass
    
    def update_display(self):
        pass
    
    def update_control(self):
        pass

class Physics:
    def __init__(self):
        pass
    
    def register_actor(self, actor):
        pass #TODO: dasfuudasefdg

class Actor:
    def __init__(self):
        
        

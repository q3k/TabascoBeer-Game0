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
        self._active_stack = {}
        self._event_stack[name] = self._active_stack
    
    def remove_stack(self, name):
        if name in _event_stack:
            #TODO event stack remove
            for event_type in _event_stack:
                pass
    
    def event_listen(self, event):
        if self._active_stack:
            if event.type in self._active_stack:
                self._active_stack[event.type].append(event)
    
    def event_emit(self, event):
        if event.type in self._event_bindings:
            for event_prototype in self._event_bindings

class Event:
    def _respects_pattern_of(self, event):
        """Override this method to, for instance, check for presses of a key"""
        return True

class KeyPress(Event):
    type = "KeyPress"
    
    def __init__(self, key, modifiers=[]):
        self.key = key
        self.modifiers = modifiers
    
    def _respects_pattern_of(self, event):
        pass #TODO

class MousePress(Event):
    def __init__(self, button):
        pass


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
        
        

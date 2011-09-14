class EventHub:
    def __init__(self):
        self._listeners = {}
    
    def register_listener(self, listener, *args, **kwargs):
        if listener in self._listeners:
            self._listeners[listener].append()


class Event:
    pass

class KeyPress(Event):
    pass

class MousePress


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
        
        

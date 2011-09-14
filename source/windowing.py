import pyglet

from event import Event, EventHandler

class Windowing(EventHandler):
    def __init__(self):
        pass
    
    def update_display(self):
        pass
    
    def update_control(self):
        pass

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

import pyglet

from view import ViewLimitedEvent
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

class MousePress(Event, ViewLimitedEvent):
    type = "MousePress"
    def __init__(self, x, y, button):
        self.x = x
        self.y = y
        self.button = button

class MouseMove(Event, ViewLimitedEvent):
    type = "MouseMove"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Mouse Move to %i, %i" % (self.x, self.y)
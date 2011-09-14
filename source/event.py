"""
Stacks are used for house-keeping. Nothing more.
Event-callback bonds need only be recorded in _event_bindings to work.

_event_stacks = {MAIN MENU: [Event: [(callback, args, kwargs), ...]]}

_event_bindings = {EVENT TYPE: {
    Event: [(callback, args, kwargs), ...]
    }
}

"""

class EventHandler(object):
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
    
    def event_listen(self, event, callback, *args, **kwargs):
        if not event.type in self._event_bindings:
            self._event_bindings[event.type] = {}
        if not event in self._event_bindings[event.type]:
            self._event_bindings[event.type][event] = []
        self._event_bindings[event.type][event].append((callback, args, kwargs))
        
        if self._active_stack:
            if not event in self._active_stack:
                self._active_stack[event] = []
            self._active_stack[event].append(callback)
    
    def event_unlisten(self, event, callback):
       pass #TODO
    
    def event_emit(self, event):
        if event.type in self._event_bindings:
            for event_prototype in self._event_bindings:
                if event._respects_pattern_of(event_prototype):
                    pass #TODO

class Event:
    type = None
    def _respects_pattern_of(self, event):
        """Override this method to, for instance, check for presses of a key"""
        return True
    
    def __eq__(self, other):
        return self._respects_pattern_of(other) and other._respects_pattern_of(self)
    
    def __hash__(self):
        return 7#self._respects_pattern_of.__hash__()

if __name__ == '__main__':
    anus = EventHandler()
    gay = Event()
    throb = lambda: None
    
    anus.event_listen(gay, throb)
    print anus._event_bindings

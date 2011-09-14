"""
Stacks are used for house-keeping. Nothing more.
Event-callback bonds need only be recorded in _event_bindings to work.

_event_stacks = {MAIN MENU: [Event: [callback, ...]]}

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
        self._event_stacks[name] = self._active_stack
    
    def remove_stack(self, name):
        if name in self._event_stacks:
            for event in self._event_stacks[name]:
                for callback in self._event_stacks[name][event]:
                    self.event_unlisten(event, callback)
            del(self._event_stacks[name])
        self._active_stack = None
    
    def event_listen(self, event, callback, *args, **kwargs):
        if not event._type in self._event_bindings:
            self._event_bindings[event._type] = {}
        if not event in self._event_bindings[event._type]:
            self._event_bindings[event._type][event] = []
        self._event_bindings[event._type][event].append((callback, args, kwargs))
        
        if self._active_stack is not None:
            if not event in self._active_stack:
                self._active_stack[event] = []
            self._active_stack[event].append(callback)
    
    def event_unlisten(self, event, callback):
       if event._type in self._event_bindings:
           if event in self._event_bindings[event._type]:
               removal_queue = []
               for callback2 in self._event_bindings[event._type][event]:
                   if callback2[0] == callback:
                       removal_queue.append(callback2)
               for callback2 in removal_queue:
                   self._event_bindings[event._type][event].remove(callback2)
    
    def event_emit(self, event):
        if event._type in self._event_bindings:
            for event_prototype in self._event_bindings:
                if event._respects_pattern_of(event_prototype):
                    pass #TODO

class Event:
    _type = None
    def _respects_pattern_of(self, event):
        """Override this method to implement more complex events"""
        return True
    
    def __eq__(self, other):
        return self._respects_pattern_of(other) and other._respects_pattern_of(self)
    
    def __hash__(self):
        return self._type.__hash__()

if __name__ == '__main__':
    anus = EventHandler()
    anus2 = EventHandler()
    gay = Event()
    throb = lambda: None
    
    print "Testing event listening"
    anus.event_listen(gay, throb)
    anus.event_listen(gay, throb)
    print anus._event_bindings
    
    print "Testing event unlistening"
    anus.event_unlisten(gay, throb)
    print anus._event_bindings
    
    print "Testing event stack adding"
    anus.add_stack('Giovanna')
    anus.event_listen(gay, throb)
    print anus._event_stacks
    
    print "Testing event stack removal"
    anus.remove_stack('Giovanna')
    print anus._event_stacks
    
    print "Testing multiple event handlers"
    anus2.event_listen(gay, throb)
    print anus2._event_bindings

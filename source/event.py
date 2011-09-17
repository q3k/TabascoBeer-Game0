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
        EventHandler._active_stack = {}
        EventHandler._event_stacks[name] = EventHandler._active_stack
    
    def remove_stack(self, name):
        if name in EventHandler._event_stacks:
            for event in EventHandler._event_stacks[name]:
                for callback in EventHandler._event_stacks[name][event]:
                    self.event_unlisten(event, callback)
            del(EventHandler._event_stacks[name])
        EventHandler._active_stack = None
    
    def event_listen(self, event, callback, *args, **kwargs):
        if not event._type in EventHandler._event_bindings:
            EventHandler._event_bindings[event._type] = {}
        if not event in EventHandler._event_bindings[event._type]:
            EventHandler._event_bindings[event._type][event] = []
        EventHandler._event_bindings[event._type][event].append((callback, args, kwargs))
        
        if EventHandler._active_stack is not None:
            if not event in EventHandler._active_stack:
                EventHandler._active_stack[event] = []
            EventHandler._active_stack[event].append(callback)
    
    def event_unlisten(self, event, callback):
        if event._type in EventHandler._event_bindings:
            if event in EventHandler._event_bindings[event._type]:
                removal_queue = []
                for callback2 in EventHandler._event_bindings[event._type][event]:
                    if callback2[0] == callback:
                        removal_queue.append(callback2)
                for callback2 in removal_queue:
                    EventHandler._event_bindings[event._type][event].remove(callback2)
    
    def event_emit(self, event):
        if event._type in EventHandler._event_bindings:
            for event_prototype in EventHandler._event_bindings[event._type]:
                if event._respects_pattern_of(event_prototype):
                    for callback, args, kwargs in EventHandler._event_bindings[event._type][event_prototype]:
                        callback(*args, **kwargs)

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
    gay = Event()
    def throb(*args, **kwargs):
        print "throbbcock gayfarer", args, kwargs
    
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
    
    anus2 = EventHandler()
    anus3 = EventHandler()
    
    print "Testing multiple event handlers"
    anus2.event_listen(gay, throb, 69, some=3)
    print anus2._event_bindings
    anus3.event_listen(gay, throb)
    anus3.event_listen(gay, throb)
    print anus3._event_bindings
    
    print "Testing event emitting"
    anus.event_emit(gay)

'''
Created on Sep 17, 2011

@author: q3k

The nomenclature of these classes is shamelessly ripped from iOS.
Don't sue me, Apple.
'''

class BaseView(object):
    '''
    A basic view that does shit nothing, but can be pushed onto a
    ViewController stack.
    A View is a 'screen' that is currently active, and a stack of these (with
    the topmost being the active one) is present in a ViewController, usually.
    Only the topmost view is being actively called by the game events - you can
    think of this as screen multiplexing. When a view is called it can,
    however, call lower views from the stack (to draw transparency or
    whatever).
    '''


    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        self.position = (0, 0)
        self.size = (1, 1)
        self.catch_all_events = False
        self.pass_events_to_upper = True
        
        # what the hack
        self.__dict__.update(kwargs)
        
        self.upper_view = None
    
    def draw(self):
        '''
        Draw yo' shit here.
        '''
        pass
    
    def process_event_unfiltered(self, event):
        '''
        You don't have to override this - it's a function that will dispatch
        events according to their type and if they fit in our screen
        coordinates.
        '''
        
        if self.catch_all_events:
            self.process_event(event)
            return
        
        if hasattr(event, "affects_view"):
            if event.affects_view(self):
                self.process_event(event)
            elif self.pass_events_to_upper and self.upper_view:
                self.upper_view.process_event_unfiltered(event)
        else:
            self.process_event(event)
    
    def process_event(self, event):
        '''
        This is called when the event surely is important to us.
        Override me.
        '''
        pass

class ViewController(object):
    '''
    The name has nothing to do with the C of MVC.
    '''
    def __init__(self):
        self._stack = []
    
    @property
    def top(self):
        if len(self._stack) < 1:
            raise Exception("ViewController stack empty, bro!")
        
        return self._stack[-1]
    
    def push(self, view):
        self._stack.append(view)
        
        if len(self._stack) > 1:
            view.upper_view = self._stack[-2]
    
    def pop(self):
        self.top.upper_view = None        
        self._stack.pop()
    
    def draw(self):
        self.top.draw()
    
    def process_event(self, event):
        self.top.process_event_unfiltered(event)

class ViewLimitedEvent(object):
    '''
    Events can derive from this if they wish to be filtered based on their
    x and y members.
    '''
    
    def affects_view(self, view):
        (x0, y0) = view.position
        (w0, h0) = view.size
        
        if x0 < self.x < x0 + w0 and y0 < self.y < y0 + h0:
            return True
        
        return False

if __name__ == "__main__":
    vc = ViewController()
    
    class DebugView(BaseView):
        def draw(self):
            print "%s: DRAWING" % str(self)
        
        def process_event(self, event):
            print "%s: THIS HAPPENED: %s" % (str(self), str(event))
        
        def __str__(self):
            return "DebugView %04i,%04i %04i,%04i @%08x" % (self.position[0],
                                                            self.position[1],
                                                            self.size[0],
                                                            self.size[1],
                                                            id(self))
    
    dv0 = DebugView(position=(0, 0), size=(800, 600))
    vc.push(dv0)
    
    vc.draw()
    
    from windowing import MouseMove
    mm0 = MouseMove(10, 10)
    mm1 = MouseMove(1000, 1000)
    
    vc.process_event(mm0)
    vc.process_event(mm1)
    
    dv1 = DebugView(position=(500, 500), size=(1000, 1000))
    vc.push(dv1)
    
    vc.process_event(mm0)
    vc.process_event(mm1)
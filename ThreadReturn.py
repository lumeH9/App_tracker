from threading import Thread

# creating new class that can return the thread result
# Standard Thread class can't return result of thread

class ThreadWithReturnValue(Thread):
    def __init__(self, *init_args, **init_kwargs):
        Thread.__init__(self, *init_args, **init_kwargs)
        self._return = None
    def run(self):
        self._return = self._target(*self._args, **self._kwargs)
    def join(self):
        Thread.join(self)
        return self._return
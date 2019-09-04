name = "example_pkg"
import itertools
import threading
import time
import sys

def construct(expression, var="x"):
    """Constructs a function, assign function return to a variable"""
    def f(x):
        return eval(expression.replace(var, "x"))
    return f

class loading():
    """Loading class"""
    def start(self, flavor="loading"):
        """Starts a loading sequence"""
        self.done=False
        self.flavor = flavor
        t = threading.Thread(target=self.animate, daemon=True)
        t.start()

    def stop(self):
        "Stops a loading sequence"
        self.done=True
        time.sleep(0.2)

    def animate(self):
        "DO NOT USE, internal function"
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if self.done:
                break
            sys.stdout.write(f'\r{self.flavor} ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')
        sys.stdout.flush()
        sys.stdout.write("\n")
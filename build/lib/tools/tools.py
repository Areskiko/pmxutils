name = "example_pkg"
import itertools
import threading
import time
import sys

def construct(expression, var="x"):
    def f(x):
        return eval(expression.replace(var, "x"))
    return f

class loading():
    def start(self, flavor="loading"):
        self.done=False
        self.flavor = flavor
        t = threading.Thread(target=self.animate, daemon=True)
        t.start()

    def stop(self):
        self.done=True
        time.sleep(0.2)

    def animate(self):
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if self.done:
                break
            sys.stdout.write(f'\r{self.flavor} ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')
        sys.stdout.flush()
        sys.stdout.write("\n")
from bottle import *
import threading
import time

BUS, THREAD = 0, 1


class Timer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = True
        self.BASE_TIME = 20
        self.time = self.BASE_TIME

    def set_instance(self, bus):
        self.bus = bus
        bus.set_instance(self)
        return bus, self

    def run(self):
        while self.running:
            time.sleep(0.1)
            if self.time > 0:
                self.time -= 1
            else:
                self.bus.leave()
    
    def kill(self):
        self.running = False

    def reset(self):
        self.time = self.BASE_TIME



class Bus:
    def __init__(self):
        self.is_arrived = False

    def set_instance(self, thread):
        self.thread = thread
        thread.start()

    def arrive(self):
        self.is_arrived = True
        self.thread.reset()

    def leave(self):
        self.is_arrived = False


bus_map = {"hachioji": Timer().set_instance(Bus())}
print("annn")


@get("/bus/<location>")
def bus(location):
    bus_map[location][BUS].arrive()


@get("/data/<location>")
def data(location):
    return "到着" if bus_map[location][BUS].is_arrived else "まだ"


class Loop(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = True
        self.printed = False

    def run(self):
        while self.running:
            time.sleep(0.1)
            if bus_map["hachioji"][BUS].is_arrived and self.printed:
                pass
            elif not bus_map["hachioji"][BUS].is_arrived:
                self.printed = False


if __name__ == "__main__":
    loop = Loop()
    print(__name__)
    loop.start()
    run(host="0.0.0.0", port=8000)

    for k, v in bus_map.items():
        v[THREAD].kill()
    loop.running = False

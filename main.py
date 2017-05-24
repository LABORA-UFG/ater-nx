import time
import multiprocessing
import time
from random import randint

from rx import Observable, Observer

from app_start import AppStart


def push_five_strings(observer):
    observer.on_next("Alpha")
    time.sleep(2)
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()

class PrintObserver(Observer):
    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))


class PrintObserver2(Observer):
    def on_next(self, value):
        print("Received 2 {0}".format(value))

    def on_completed(self):
        print("Done 2 !")

    def on_error(self, error):
        print("Error Occurred 2 : {0}".format(error))

def main():
    # # calculate number of CPU's, then create a ThreadPoolScheduler with that number of threads
    # optimal_thread_count = multiprocessing.cpu_count()
    # source = Observable.create(push_five_strings)
    # source.subscribe(PrintObserver())
    #
    # print 'ok'

    # Observable.interval(1000).map(lambda i: "{0} Mississippi".format(i)) .subscribe(PrintObserver())
    #

    # three_emissions = Observable.range(1, 5)
    #
    # three_random_ints = three_emissions.map(lambda i: randint(1, 100000)).publish().auto_connect(2)
    #
    # a = PrintObserver()
    # three_random_ints.subscribe(a)
    # three_random_ints.subscribe(PrintObserver2())

    app = AppStart()



if __name__ == "__main__":
    main()

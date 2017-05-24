from rx import Observer

from abs_hal import AbsHal
from of_interface import OFInterface


class PrintObserver(Observer):
    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))


class AppStart(OFInterface):
    def __init__(self):
        print 'AppStart::__init__'
        self.hal = AbsHal()
        self.hal.add_subs(PrintObserver())
        self.hal.send()

    def send_flow_mod(self, dp):
        pass

    def flow_removed_handler(self, ev):
        pass

    def send_flow_stats_request(self, dp):
        pass

    def send_desc_stats_request(self, dp):
        pass

    def desc_stats_reply_handler(self, ev):
        pass

    def packet_in_handler(self, ev):
        pass

# Copyright (c) 2017-2017, RNP (http://www.rnp.br)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# Neither the name of the RNP nor the names of its contributors may be used to
# endorse or promote products derived from this software without specific
# prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from hal.brocade_hal import BrocadeHal
from monitor.statistics_monitor import StatisticsMonitor
from of.of_interface import OFHandler


class AppStart(OFHandler):
    def __init__(self):
        # Get type of hal from configuration file
        self.hal = BrocadeHal()

        # --------------------------------------
        # Start class that use this hal
        # --------------------------------------
        # ::StatisticsMonitor::
        self.stats_monitor = StatisticsMonitor(self.hal)

    # ------ handler ---------
    def switch_enter_handler(self, ev):
        self.hal.switch_enter_handler(ev)

    def switch_leave_handler(self, ev):
        self.hal.switch_leave_handler(ev)

    def packet_in_handler(self, ev):
        self.hal.packet_in_handler(ev)

    def desc_stats_reply_handler(self, ev):
        self.hal.desc_stats_reply_handler(ev)

    def flow_removed_handler(self, ev):
        self.hal.flow_removed_handler(ev)

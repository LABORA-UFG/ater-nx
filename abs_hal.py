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
from rx import Observable
from rx.subjects import Subject

from of_interface import OFInterface


class AbsHal(OFInterface):

    def __init__(self):
        print 'AbsHal::init'
        self.observer = Observable.create(self.__create_observer)
        # self.stream = Subject()

    def __create_observer(self, observer):
        print 'AbsHal::__create_observer'
        self.observer = observer

    def add_subs(self, listener):
        print 'AbsHal::__add_subs'
        self.observer.subscribe(listener)
        # self.stream.on_next(10)

    def send(self):
        print 'AbsHal::send'
        self.observer.on_next('mess 1')
        self.observer.on_next('mess 2')

    def send_flow_mod(self, dp):
        pass

    def send_flow_stats_request(self, dp):
        pass

    def send_desc_stats_request(self, dp):
        pass

    def desc_stats_reply_handler(self, ev):
        self.observer.on_next(ev)

    def packet_in_handler(self, ev):
        pass

    def flow_removed_handler(self, ev):
        pass
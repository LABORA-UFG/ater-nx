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

from abc import ABCMeta, abstractmethod


class OFObservable(object):
    pass


class OFPacketIn(OFObservable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def packet_in_handler(self, ev):
        return NotImplemented


class OFDescStatsReply(OFObservable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def desc_stats_reply_handler(self, ev):
        return NotImplemented


class OFFlowRemoved(OFObservable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def flow_removed_handler(self, ev):
        return NotImplemented


class OFSwitchEnter(OFObservable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def switch_enter_handler(self, ev):
        return NotImplemented


class OFSwitchLeave(OFObservable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def switch_leave_handler(self, ev):
        return NotImplemented


class OFHandler(OFPacketIn, OFDescStatsReply, OFFlowRemoved, OFSwitchEnter, OFSwitchLeave):
    __metaclass__ = ABCMeta


class OFSend(OFObservable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def send_flow_mod(self, dp):
        return NotImplemented

    @abstractmethod
    def send_desc_stats_request(self, dp):
        return NotImplemented

    @abstractmethod
    def send_flow_stats_request(self, dp):
        return NotImplemented

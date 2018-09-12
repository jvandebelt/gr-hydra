#!/usr/bin/python2
#
# Copyright 2005,2006,2011 Free Software Foundation, Inc.
# 
# This file is part of GNU Radio
# 
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr
from gnuradio import blocks
from gnuradio.digital import ofdm_mod

import sys
import threading
import struct
import logging

import SimpleXMLRPCServer


class XMLRPCThread(threading.Thread):
    def __init__(self, ipaddr, buffersize, tx_path):
        threading.Thread.__init__(self)

        self._value = 70
        self._buffersize = buffersize
        self._tx_path = tx_path
        self._run = True
        self.xmlrpc_server = SimpleXMLRPCServer.SimpleXMLRPCServer((ipaddr, 22345), allow_none=True)

        self.xmlrpc_server.register_instance(self)
        threading.Thread(target=self.xmlrpc_server.serve_forever).start()

    def set_value(self, value):
        self._value = value

    def run(self):
        pktno = 0
        n = 0

        while self._run:
            # pdb.set_trace()
            # try:
            """
            data = s.recv(options.bufferbytes)
            """
            print "-"
            data = struct.pack('!H', 0xaaaa) + str(self._value) + " ".join(["" for x in range(400)])
            payload = data
            self._tx_path.send_pkt(payload)
            n += len(payload)

            pktno += 1

        logging.info("tx_bytes = %d,\t tx_pkts = %d" % (n, pktno))
        self._tx_path.send_pkt(eof=True)
        self.xmlrpc_server.stop()


class ReadThread(threading.Thread):
    def __init__(self, filename, buffersize, tx_path, read_from_beginning = False):

        threading.Thread.__init__(self)

        self._run = True
        self._filename = filename
        self._buffersize = buffersize
        self._tx_path = tx_path
        self._read = read_from_beginning


    def run(self):
        f = open(self._filename, "rb")

        pktno = 0
        n = 0

        while self._run:
            # pdb.set_trace()
            # try:
            """
            data = s.recv(options.bufferbytes)
            """
            print "."
            if self._read:
                  f = open(self._filename, "rb")

            data = f.read(self._buffersize)

            if not data:
                print("starting from beginning")
                f.seek(0)
                data = f.read(self._buffersize)

            # transmit the same pkt 2 times. Receiver can throw away one in case of errors
            payload = struct.pack('!H', 0xffff & 0) + data
            self._tx_path.send_pkt(payload)

            payload = struct.pack('!H', 0xffff & 1) + data
            self._tx_path.send_pkt(payload)

            n += len(payload)

            pktno += 1
            pktno %= 2

        logging.info("tx_bytes = %d,\t tx_pkts = %d" % (n, pktno))
        self._tx_path.send_pkt(eof=True)
        f.close()


# /////////////////////////////////////////////////////////////////////////////
#                              transmit path
# /////////////////////////////////////////////////////////////////////////////
class TransmitPath(gr.hier_block2):
    def __init__(self, options):
        '''
        See below for what options should hold
        '''
        gr.hier_block2.__init__(self, "transmit_path",
                                gr.io_signature(0, 0, 0),
                                gr.io_signature(1, 1, gr.sizeof_gr_complex))

        # digital amp inside gnuradio radio
        self._tx_amplitude = options.tx_amplitude

        self.ofdm_tx = ofdm_mod(options,
                                msgq_limit=4,
                                pad_for_usrp=False)

        self.amp = blocks.multiply_const_cc(1)
        self.set_tx_amplitude(self._tx_amplitude)

        # Create and setup transmit path flow graph
        self.connect(self.ofdm_tx, self.amp, self)

        if options.file is None:
            logging.error("Filename is empty")
            sys.exit(0)

    def set_tx_amplitude(self, ampl):
        """
        Sets the transmit amplitude sent to the USRP

        Args:
            : ampl 0 <= ampl < 1.0.  Try 0.10
        """
        self._tx_amplitude = max(0.0, min(ampl, 1))
        self.amp.set_k(self._tx_amplitude)

    def send_pkt(self, payload='', eof=False):
        """
        Calls the transmitter method to send a packet
        """
        return self.ofdm_tx.send_pkt(payload, eof)

    def _print_verbage(self):
        """
        Prints information about the transmit path
        """
        print("Tx amplitude     %s" % (self._tx_amplitude))

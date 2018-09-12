#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Hydra Gr Client Example
# Generated: Wed Aug 15 11:17:49 2018
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import hydra
import sip
import sys
import threading
from gnuradio import qtgui


class hydra_gr_client_example(gr.top_block, Qt.QWidget):

    def __init__(self, freq=949.5e6, samp_rate=200e3):
        gr.top_block.__init__(self, "Hydra Gr Client Example")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Hydra Gr Client Example")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "hydra_gr_client_example")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.mul2 = mul2 = 0.1
        self.mul1 = mul1 = 0.1

        ##################################################
        # Blocks
        ##################################################
        self._mul2_range = Range(0, 1, 0.01, 0.1, 200)
        self._mul2_win = RangeWidget(self._mul2_range, self.set_mul2, 'mul2', "counter_slider", float)
        self.top_layout.addWidget(self._mul2_win)
        self._mul1_range = Range(0, 1, 0.01, 0.1, 200)
        self._mul1_win = RangeWidget(self._mul1_range, self.set_mul1, 'mul1', "counter_slider", float)
        self.top_layout.addWidget(self._mul1_win)
        self.qtgui_waterfall_sink_x_2_0 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_2_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_2_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_2_0.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_2_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_2_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_2_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_2_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_2_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_2_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_2_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_2_0_win)
        self.qtgui_waterfall_sink_x_2 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_2.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_2.enable_grid(False)
        self.qtgui_waterfall_sink_x_2.enable_axis_labels(True)

        if not True:
          self.qtgui_waterfall_sink_x_2.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_2.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_2.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_2.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_2.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_2_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_2_win)
        self.qtgui_histogram_sink_x_0_1_0 = qtgui.histogram_sink_f(
        	1024,
        	100,
                -1,
                1000,
        	"Data Rcv VR2",
        	1
        )

        self.qtgui_histogram_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0_1_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0_1_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0_1_0.enable_grid(False)
        self.qtgui_histogram_sink_x_0_1_0.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_histogram_sink_x_0_1_0_win)
        self.qtgui_histogram_sink_x_0_1 = qtgui.histogram_sink_f(
        	1024,
        	100,
                -1,
                1000,
        	"Data Rcv VR1",
        	1
        )

        self.qtgui_histogram_sink_x_0_1.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0_1.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0_1.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0_1.enable_grid(False)
        self.qtgui_histogram_sink_x_0_1.enable_axis_labels(True)

        if not True:
          self.qtgui_histogram_sink_x_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_1_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_histogram_sink_x_0_1_win)
        self.hydra_gr_sink_0_0 = hydra.hydra_gr_client_sink(3, '127.0.0.1', 5000)
        self.hydra_gr_sink_0_0.start_client(freq + 1e6, samp_rate, 1024)
        self.hydra_gr_sink_0 = hydra.hydra_gr_client_sink(1, '127.0.0.1', 5000)
        self.hydra_gr_sink_0.start_client(freq, samp_rate * 1.5, 1024)
        self.hydra_gr__source_0_0_0 = hydra.hydra_gr_client_source(2, '127.0.0.1', 5000)
        self.hydra_gr__source_0_0_0.start_client(freq + 1e6, samp_rate, 10000)

        self.hydra_gr__source_0_0 = hydra.hydra_gr_client_source(1, '127.0.0.1', 5000)
        self.hydra_gr__source_0_0.start_client(freq, samp_rate * 1.5, 10000)

        self.digital_ofdm_tx_0 = digital.ofdm_tx(
        	  fft_len=64, cp_len=16,
        	  packet_length_tag_key="len",
        	  bps_header=1,
        	  bps_payload=1,
        	  rolloff=0,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.digital_ofdm_rx_0_0 = digital.ofdm_rx(
        	  fft_len=64, cp_len=16,
        	  frame_length_tag_key='frame_'+"len",
        	  packet_length_tag_key="len",
        	  bps_header=1,
        	  bps_payload=1,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.digital_ofdm_rx_0 = digital.ofdm_rx(
        	  fft_len=64, cp_len=16,
        	  frame_length_tag_key='frame_'+"len",
        	  packet_length_tag_key="len",
        	  bps_header=1,
        	  bps_payload=1,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.blocks_vector_source_x_0 = blocks.vector_source_b([x for x in range(0,250)], True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 200e3,True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, 100, "len")
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((mul2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((mul1, ))
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_histogram_sink_x_0_1, 0))
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_histogram_sink_x_0_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.hydra_gr_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.hydra_gr_sink_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.digital_ofdm_rx_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_ofdm_rx_0_0, 0), (self.blocks_char_to_float_0_0, 0))
        self.connect((self.digital_ofdm_tx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.hydra_gr__source_0_0, 0), (self.digital_ofdm_rx_0, 0))
        self.connect((self.hydra_gr__source_0_0, 0), (self.qtgui_waterfall_sink_x_2, 0))
        self.connect((self.hydra_gr__source_0_0_0, 0), (self.digital_ofdm_rx_0_0, 0))
        self.connect((self.hydra_gr__source_0_0_0, 0), (self.qtgui_waterfall_sink_x_2_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hydra_gr_client_example")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_2_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_2.set_frequency_range(0, self.samp_rate)

    def get_mul2(self):
        return self.mul2

    def set_mul2(self, mul2):
        self.mul2 = mul2
        self.blocks_multiply_const_vxx_0_0.set_k((self.mul2, ))

    def get_mul1(self):
        return self.mul1

    def set_mul1(self, mul1):
        self.mul1 = mul1
        self.blocks_multiply_const_vxx_0.set_k((self.mul1, ))


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=hydra_gr_client_example, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()

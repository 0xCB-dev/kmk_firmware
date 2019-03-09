import board

from kmk.consts import DiodeOrientation
from kmk.mcus.circuitpython_samd51 import Firmware as _Firmware
from kmk.pins import Pin as P


class Firmware(_Firmware):
    col_pins = (P.A0, P.A1, P.A2, P.A3, P.A4, P.A5, P.SCK, P.MOSI)
    row_pins = (P.TX, P.RX, P.SDA, P.SCL, P.D13, P.D12, P.D11, P.D10)
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.D9
    rgb_num_pixels = 12

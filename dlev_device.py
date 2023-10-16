"""
    Class to encapsulate the D-Lev Device
"""

import rtmidi
import mido


class dlev_device(object):
    """This class handles all access to the D-Lev MIDI USB device"""

    _device_name = "D-Lec Midi 1"
    _output_port = 0

    def __init__(self):
        super(dlev_device, self).__init__()

    def open(self):
        """
        Open the default D-Lev MIDI device

        The default name on Windows has a "1" appended, this
        may not be consistent and further processing may be required to
        discover the actual device name.

        """
        output_devices = mido.get_output_names()
        try:
            d_lec_index = output_devices.index(self._device_name)
            _output_port = mido.open_output(output_devices[d_lec_index])
        except Exception as e:
            raise e


if __name__ == "__main__":
    device = dlev_device()
    device.open()
    print("Done")
    pass

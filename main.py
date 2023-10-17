#
#  Test module for D-Lec MIDI USB ports
#

from dlev_device import dlev_device
from dlev_sysex import dlev_sysex


def main():
    device = dlev_device()
    device.open()
    sysex_msg = dlev_sysex("status")
    device.send(sysex_msg)

    print("main done")


if __name__ == "__main__":
    main()

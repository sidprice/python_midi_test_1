# 
#  Test module for D-Lec MIDI USB ports
# 

import rtmidi
import mido

def main():
    output_devices = mido.get_output_names()
    d_lec_index = output_devices.index('D-Lec Midi 1')
    port = mido.open_output(output_devices[d_lec_index])
    print(f"Using device \"{output_devices[d_lec_index]}\"")
    print("Send a CC message as a test")
    msg = mido.Message('note_on', note=72)
    port.send(msg)

if __name__ == "__main__":
    main()

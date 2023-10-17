""" Class to encapsulate D-Lev SysEx messages """

from mido import Message


class dlev_sysex(object):
    """Class for processing D-Lev SysEx messages

    This class uses a list of defined D-Lev SysEx messages.

    For sending, it looks up a text-based SysEx message, formats
    the MIDI message, and sends it to the configured port.

    For received messages, it parses the message and returns
    a text-base name and value, or reports an error. On error
    it raises an exception.
    """

    _dev_l_sysex_messages = {"status": [0x01, 0x02, 0x03], "hcl": [0x02]}

    def __init__(self, name):
        self.msg = Message("sysex")
        self.name = name
        self.content = self._dev_l_sysex_messages[name]
        self.msg.data = bytes(self.content)

    def get_name(self):
        """Return the name of this sysex"""
        return self.name

    def get_content(self):
        """Return the content for this sysex message"""
        return self.content

    def get_message(self):
        return self.msg


if __name__ == "__main__":
    msg = dlev_sysex("status")
    print(msg.get_name())
    print(msg.get_content())

# msg.send('status')

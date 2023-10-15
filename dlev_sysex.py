""" Class to encapsulate D-Lev SysEx messages """

class d_lev_sysex_message(object):
    """ Class for processing D-Lev SysEx messages
    
        This class uses a list of defined D-Lev SysEx messages.

        For sending, it looks up a text-based SysEx message, formats
        the MIDI message, and sends it to the configured port.

        For received messages, it parses the message and returns
        a text-base name and value, or reports an error. On error
        it raises an exception.
    """

    _dev_l_sysex_messages = {
        'status' : 'send_states',
        'hcl' : "select_hcl"
    }

    _name = ""   """ The name of the SysEx message """
    _content = ""    """ The content sent to the MIDI device for this sysex command """

    def __init__(self, name):
        super(d_lev_sysex_message, self).__init__()
        self._name = name
        self._content = self._dev_l_sysex_messages[name]

    def get_name(self):
        """ Return the name of this sysex """
        return self._name

    def get_content(self):
        """ Return the formatted content for this sysex message """
        return self._content

    def send(self, sysex_name):
        pass

if __name__ == "__main__":
    msg = d_lev_sysex_message("status")
    print(msg.get_name())
    print(msg.get_content())

# msg.send('status')

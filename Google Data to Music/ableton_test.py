import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print (available_ports)

if available_ports: 
    midiout.open_port(1)
else: 
    midiout.open_virtual_port("My virtual output")

note_on = [0x90, 60, 112]
note_off = [0x80, 60, 0]
midiout.send_message(note_on)
time.sleep(0.5) 
# I tried running the script without having to invoke the sleep function but it doesn't work. 
# If someone could enlighten me as to why this is, I'd be more than grateful.
midiout.send_message(note_off)

del midiout
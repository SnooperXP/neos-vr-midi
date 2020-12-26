from midi.midi_input import *

class MidiData:
	def __init__(self, clock, event):
		self.clock = clock
		self.event = event

class MidiDevice:
	def __init__(self, midi, midi_menu):
		self.device = midi_menu.get_device(midi)

	def poll_device(self):
		if self.device.poll():
			event = self.device.read(1)[0]
			midi_input_raw = MidiInputRaw(event[0][0], event[0][1:])
			return MidiData(event[1], midi_input_raw.map())
		return None

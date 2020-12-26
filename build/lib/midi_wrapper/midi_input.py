class MidiInput:
	def __init__(self, name, channel=None):
		self.name = name
		self.channel = channel

class MidiInputNoteOff(MidiInput):
	def __init__(self, channel, note_number, note_velocity):
		MidiInput.__init__(self, "Note_off", channel)
		self.data = {
			"note_number": note_number,
			"note_velocity": note_velocity
		}

class MidiInputNoteOn(MidiInput):
	def __init__(self, channel, note_number, note_velocity):
		MidiInput.__init__(self, "Note_on", channel)
		self.data = {
			"note_number": note_number,
			"note_velocity": note_velocity
		}

class MidiInputPolyphonicAftertouch(MidiInput):
	def __init__(self, channel, note_number, aftertouch_pressure):
		MidiInput.__init__(self, "Polyphonic_aftertouch", channel)
		self.data = {
			"note_number": note_number,
			"aftertouch_pressure": aftertouch_pressure
		}

class MidiInputControlModeChange(MidiInput):
	def __init__(self, channel, number, value):
		MidiInput.__init__(self, "Control_mode_change", channel)
		self.data = {
			"number": number,
			"value": value
		}

class MidiInputProgramChange(MidiInput):
	def __init__(self, channel, program):
		MidiInput.__init__(self, "Program_change", channel)
		self.data = {
			"program": program
		}

class MidiInputChannelAftertouch(MidiInput):
	def __init__(self, channel, aftertouch_pressure):
		MidiInput.__init__(self, "Channel_aftertouch", channel)
		self.data = {
			"aftertouch_pressure": aftertouch_pressure
		}

class MidiInputPitchWheelRange(MidiInput):
	def __init__(self, channel, least_significant, most_significant):
		MidiInput.__init__(self, "Pitch_wheel_range", channel)
		self.data = {
			"least_significant": least_significant,
			"most_significant": most_significant
		}

class MidiInputSystemExclusive(MidiInput):
	def __init__(self, vendor_id, value):
		MidiInput.__init__(self, "System_exclusive")
		self.data = {
			"value": value
		}

class MidiInputSystemUndefined(MidiInput):
	def __init__(self, data):
		MidiInput.__init__(self, "System_undefined")
		self.data = data

class MidiInputSongPositionPointer(MidiInput):
	def __init__(self, least_significant, most_significant):
		MidiInput.__init__(self, "Song_position_pointer")
		self.data = {
			"least_significant": least_significant,
			"most_significant": most_significant
		}

class MidiInputTuneRequest(MidiInput):
	def __init__(self):
		MidiInput.__init__(self, "Tune_request")

class MidiInputEndOfSysEx(MidiInput):
	def __init__(self):
		MidiInput.__init__(self, "End_of_sys_ex")

class MidiInputRealTime(MidiInput):
	def __init__(self, event):
		MidiInput.__init__(self, f"Real_time_{event}")


class MidiInputRaw:
	def __init__(self, status, data):
		self.status = status
		self.data = data

	def map(self):
		data = self.data
		status = self.status

		if status >= 128 and status <= 143:
			return MidiInputNoteOff(status - 127, data[0], data[1])
		elif status >= 144 and status <= 159:
			return MidiInputNoteOn(status - 143, data[0], data[1])
		elif status >= 160 and status <= 175:
			return MidiInputPolyphonicAftertouch(status - 159, data[0], data[1])
		elif status >= 176 and status <= 191:
			return MidiInputControlModeChange(status - 175, data[0], data[1])
		elif status >= 192 and status <= 207:
			return MidiInputProgramChange(status - 191, data[0])
		elif status >= 208 and status <= 223:
			return MidiInputChannelAftertouch(status - 207, data[0])
		elif status >= 224 and status <= 239:
			return MidiInputPitchWheelRange(status - 223, data[0], data[1])
		elif status == 240:
			return MidiInputSystemExclusive(data[0], data[1])
		elif status == 242:
			return MidiInputSongPositionPointer(data[0], data[1])
		elif status in [241, 244, 245]:
			return MidiInputSystemUndefined(data)
		elif status == 246:
			return MidiInputTuneRequest()
		elif status == 247:
			return MidiInputEndOfSysEx()
		elif status == 248:
			return MidiInputRealTime("timing_clock")
		elif status == 250:
			return MidiInputRealTime("start")
		elif status == 251:
			return MidiInputRealTime("continue")
		elif status == 252:
			return MidiInputRealTime("stop")
		elif status == 254:
			return MidiInputRealTime("active_sensing")
		elif status == 255:
			return MidiInputRealTime("sys_reset")
		elif status in [249, 253]:
			return MidiInputRealTime("undefined")
		return None

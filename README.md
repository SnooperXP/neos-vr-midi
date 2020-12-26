# Midi Wrapper

This package contains classes that wrap the Pygame Midi class to allow selection of a midi input device, and simple polling of said device with predefined classes to help interpret the signals.

This implementation is limited in that it is only polling for one event per poll instead of multiple events, as such it will pull one at a time.

Polling for multiple events in one frame may be supported in future.

## Usage

```python
from pygame import midi
from midi_wrapper import MidiMenu, MidiDevice

# Boiler plate midi initialization for pygame midi
midi.init()

if (midi == None):
	print("Error initializing midi.")
	exit(-1)

# Initialize the menu to start device selection, then pass to device to get reference
midi_menu = MidiMenu(midi)
midi_device = MidiDevice(midi, midi_menu)

# Bog standard polling loop
while True:
	# Returns None if no events received or a MidiData type if an event is found
	midi_data = midi_device.poll_device()

	if midi_data != None:
		midi_event = midi_data.event
		print(f"Clock: {midi_data.clock} :: Name: {midi_event.name} :: Channel: {midi_event.channel} :: Data: {midi_event.data}")

```
from pygame import midi
from midi.midi_input import *
import pprint

midi.init()

supported_interfaces = ['MMSystem', 'ALSA', 'CoreMIDI']
pp = pprint.PrettyPrinter(indent=2)
print("Choose midi input device")
device_count = midi.get_count()
supported_device_ids = []

for n in range(device_count):
	current_info = midi.get_device_info(n)
	current_interface = current_info[0].decode('ascii')

	if current_interface not in supported_interfaces:
		continue

	input_supported = (current_info[2] == 1)

	if not input_supported:
		continue

	supported_device_ids.append(str(n))

	device_name = current_info[1].decode('ascii')
	device_opened = current_info[4]

	print(f"[{n}] {device_name} :: Opened: {device_opened}")

if len(supported_device_ids) == 0:
	print("No supported devices. Please ensure the devices aren't currenlty in use by another program.")
	exit()

device_id = input(f"Input device number: ")

while True:
	if device_id in supported_device_ids:
		break
	else:
		device_id = input(f"Invalid number, please input valid device number: ")

device = midi.Input(int(device_id))
print("Device connected!")

while True:
	if device.poll():
		event = device.read(1)[0]
		midi_input_raw = MidiInputRaw(event[0][0], event[0][1:])
		midi_input = midi_input_raw.map()
		print(f"Clock: {event[1]} :: Name: {midi_input.name} :: Channel: {midi_input.channel} :: Data: {midi_input.data}")

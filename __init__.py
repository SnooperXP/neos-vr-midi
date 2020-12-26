import keyboard
from midi.midi_input import *
from midi.midi_menu import MidiMenu
from midi.midi_device import MidiDevice
from pygame import midi

midi.init()

if (midi == None):
	print("Error initializing midi.")
	exit(-1)

midi_menu = MidiMenu(midi)
midi_device = MidiDevice(midi, midi_menu)

run_loop = True

while run_loop:
	midi_data = midi_device.poll_device()

	if midi_data != None:
		midi_event = midi_data.event
		print(f"Clock: {midi_data.clock} :: Name: {midi_event.name} :: Channel: {midi_event.channel} :: Data: {midi_event.data}")

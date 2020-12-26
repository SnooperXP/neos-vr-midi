class MidiMenu:
	def __init__(self, midi, supported_interfaces = ['MMSystem', 'ALSA', 'CoreMIDI']):
		self.supported_interfaces = supported_interfaces
		supported_device_ids = []
		menu_output = []
		device_count = midi.get_count()

		if device_count == 0:
			no_devices_found()

		for n in range(device_count):
			current_info = midi.get_device_info(n)
			current_interface = current_info[0].decode('ascii')

			if current_interface not in supported_interfaces:
				continue

			input_supported = (current_info[2] ==1)
			
			if not input_supported:
				continue

			supported_device_ids.append(str(n))
			device_name = current_info[1].decode('ascii')
			menu_output.append(f"[{n}] {device_name}")

		if len(supported_device_ids) == 0:
			no_devices_found(False)

		self.menu_output = menu_output
		self.supported_device_ids = supported_device_ids
		self.show_menu()

	def show_menu(self):
		print("Choose midi input device:")
		print("\n".join(self.menu_output))

		device_id = input("Input device number: ")
		self.choose_device(device_id)

	def choose_device(self, device_id):
		while True:
			if device_id in self.supported_device_ids:
				break
			else:
				device_id = input(f"Invalid number, please input valid device number: ")
		self.device_id = int(device_id)

	def no_devices_found(no_supported_devices=False):
		if no_supported_devices:
			print("No supported devices found.\n" \
				"Supported interfaces are MMSystem, ALSA, and CoreMIDI\n" \
				"Please ensure the devices aren't currently in use by another program.")
		else:
			print("No midi devices found.")
		exit(-1)

	def get_device(self, midi):
		try:
			device = midi.Input(self.device_id)
			print("Device connected!")
			return device
		except Exception as ex:
			print(f"Exception occurred while initializing device: {ex}")
			exit(-1)

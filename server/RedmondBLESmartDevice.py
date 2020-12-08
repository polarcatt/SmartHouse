class RedmondBLESmartDevice():

	def __init__(self, idd, mac, token, adapter):
		self.id = idd
		self.mac = mac
		self.token = token
		self.packageId = 1
		self.writeUuid = ""
		self.readUuid = ""
		self.state = ["notcon", "off"]
		self.address_type = pygatt.BLEAddressType.Random
		self.pairNum = 255
		self.adapter = adapter
		self.commands = {}
		commands["turnOn"] = 3
		commands["turnOff"] = 4
		commands["getInf"] = 4

	def firstConnect(self):
		connect()

	def check(self):
		pass

	def sendCommand(self, command):
		commandNum = commands[command]
		connect()
		if(device)
		conState = 2
		byteCommand = getCommandBytes(commandNum)
		self.device.char_write(writeUuid, byteCommand)
		disconnect()

	def getCommandBytes(self, commandNum, data = b''):
		conStart = b'U'
		conEnd = b'\xaa'
		return conStart + bytes([packageId]) + bytes([commandNum]) + data + conEnd

	def connect(self):
		conState = 1
		try:
			self.device = self.adapter.connect(mac, 
				address_type=self.address_type)
		except Exception:
			print("E: NoDeviceFound")
		try:
			self.device.char_write(writeUuid, getCommandBytes(pairNum, token))
		except Exception:
			print("E: NoSuchUUidinDevice")

		


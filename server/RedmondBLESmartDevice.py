class RedmondBLESmartDevice():
	
	def __init__(mac, token):
		self.mac = mac
		self.token = token
		self.packageId = 1
		self.writeUuid = ""
		self.readUuid = ""
		self.conState = 0
		self.address_type = pygatt.BLEAddressType.Random
		self.pairNum = 255

	def firstConnect(adapter):
		connect(adapter)

	def check():
		pass

	def sendCommand(command, adapter):
		commandNum = 0
		if command == "turnOn":
			commandNum = 3
		elif command == "turnOff":
			commandNum = 4
		else:
			raise NotImplemetedExpetion
		connect()
		if(device)
		conState = 2
		byteCommand = getCommandBytes(commandNum)
		self.device.char_write(writeUuid, byteCommand)
		disconnect()

	def getCommandBytes(commandNum, data = b''):
		conStart = b'U'
		conEnd = b'\xaa'
		return conStart + bytes([packageId]) + bytes([commandNum]) + data + conEnd

	def connect(adapter):
		conState = 1
		try:
			self.device = adapter.connect(mac, 
				address_type=self.address_type)
		except Exception:
			print("E: NoDeviceFound")
		try:
			self.device.char_write(writeUuid, getCommandBytes(pairNum, token))
		except Exception:
			print("E: NoSuchUUidinDevice")

		


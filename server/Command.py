class Command():

	def __init__(self, command = "", device = "1"):
		self.command = command
		self.id = device
		self.name = ""

	def GetDevice(self):
		return self.device

	def Execute(self):
		if self.command == 'Add':
			self.device.firstConnect()
			self.device.getAns(self.manageAns)
		elif self.command == 'Delete':
			self.device.con = 0
		else:
			self.device.sendCommand(command)

	def manageAns(self):
		pass

	def __str__(self):
		return str(self.__dict__)

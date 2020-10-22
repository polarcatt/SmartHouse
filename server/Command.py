class Command():

	def __init__(self, command, device):
		self.command = command
		self.device = device

	def GetDevice(self):
		return self.device

	def Execute(self):
		device.sendCommand(command)
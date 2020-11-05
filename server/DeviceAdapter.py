import socket
import pygatt
import Command 

class DeviceAdapter:
	def __init__(self):
		self.adapters = {}
		self.answers = {}
		self.adapters["BLE"] = pygatt.GATTToolBackend()
		self.devices = []
		loadDevices()
		self.commands = []
		self.packageNum = 0

	def AddCommand(self, command, deviceId):
		commands.append(Command(command, devices[deviceId]))

	def GetNextCommand(self):
		pass

	def PopCommand(self):
		pass

	def AddDevice(addr, type):
		pass

	def RemoveDevice(self):
		pass

	def CheckDevices(self):
		pass

	def GetLastState(self, device):
		pass

	def ExecuteCommand(self):
		command = GetNextCommand()
		if command:
			command.Execute(packageNum, adapter = adapters[commands.GetDevice().getDeviceType()])
			packageNum = (packageNum % 100) + 1
			answers[packageNum] = command.getAnswer()
			PopCommand()
		else:
			print("NoCommands")

	def GetDevicesInf(self):
		pass



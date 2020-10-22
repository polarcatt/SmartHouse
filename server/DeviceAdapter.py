import socket
import pygatt
import Command

class DeviceAdapter:
	def __init__():
		self.adapters = {}
		self.answers = {}
		self.adapters["BLE"] = pygatt.GATTToolBackend()
		self.devices = []
		loadDevices()
		self.commands = []
		self.packageNum = 0

	def AddCommand(command, deviceId):
		commands.append(Command(command, devices[deviceId]))

	def GetNextCommand():
		pass

	def PopCommand():
		pass

	def AddDevice():
		pass

	def RemoveDevice():
		pass

	def CheckDevices():
		pass

	def ExecuteCommand():
		commands[0].Execute(packageNum, adapter = adapters[commands.GetDevice().getDeviceType()])
		packageNum = (packageNum % 100) + 1
		answers[packageNum] = commands[0].getAnswer()
		PopCommand()

	def GetDevicesInf():
		pass



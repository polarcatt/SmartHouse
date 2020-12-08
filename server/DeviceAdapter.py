import socket
import pygatt
import Command 
import RedmondBLESmartDevice

class DeviceAdapter:
	def __init__(self):
		self.adapters = {}
		self.answers = []
		self.adapters["BLE"] = pygatt.GATTToolBackend()
		self.deviceConstruct = {"redmondBle" : ("BLE", RedmondBLESmartDevice)}
		self.devices = {}
		self.id = 0
		loadDevices()
		self.commands = []
		self.packageNum = 0

	def AddCommand(self, command, deviceId):
		commands.append(Command(command, devices[deviceId]))

	def GetNextCommand(self):
		return commands[0]

	def PopCommand(self):
		commands.remove(GetNextCommand())

	def AddDevice(self, idd):
		devices[idd].firstCon()

	def RemoveDevice(self, id):
		pass

	def CheckDevices(self):
		pass

	def ExecuteCommand(self):
		answers.append(GetNextCommand().Execute(self, packageNum, adapter = adapters[commands.GetDevice().getDeviceType()]))
		packageNum = (packageNum % 100) + 1
		PopCommand()

	def GetDevicesInf(self):
		pass



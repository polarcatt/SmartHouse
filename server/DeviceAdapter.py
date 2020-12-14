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
		self.waiting = False
		self.id = 0
		self.loadDevices()
		self.commands = []
		self.packageNum = 1

	def AddCommand(self, command):
		self.commands.append(command)

	def GetNextCommand(self):
		return self.commands[0]

	def PopCommand(self):
		self.commands.pop()

	def AddDevice(self, idd):
		devices[idd].firstCon()

	def RemoveDevice(self, id):
		pass

	def CheckDevices(self):
		pass

	def ExecuteCommand(self):
		if not self.waiting:
			self.GetNextCommand().Execute(self, self.packageNum)
		self.packageNum = (self.packageNum % 100) + 1
		self.GetNextCommand().manageAns()
		self.PopCommand()

	def GetDevicesInf(self):
		pass

	def loadDevices(self):
		pass



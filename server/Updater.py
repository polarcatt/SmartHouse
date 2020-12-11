import Server
import DeviceAdapter
import threading

class Updater:

	def __init__(self, server):
		self.deviceAdapter = DeviceAdapter.DeviceAdapter()
		self.server = server

	def UpdateDevices(self):
		for i in range(min(10, len(self.deviceAdapter.commands))):
			self.deviceAdapter.ExecuteCommand()
		self.deviceAdapter.GetDevicesInf()

	def UpdateSocket(self):
		to = self.server.getData()
		#self.server.toAnswer(to)
		self.server.logfile.flush()
		for i in to:
			self.deviceAdapter.AddCommand(i)
		print(to)

	def Update(self):
		self.UpdateSocket()
		self.UpdateDevices()


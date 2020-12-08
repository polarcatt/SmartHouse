import Server
#import DeviceAdapter
import threading

class Updater:

	def __init__(self, server):
		#self.deviceAdapter = DeviceAdapter()
		self.server = server

	def UpdateDevices(self):
		pass

	def UpdateSocket(self):
		to = self.server.getData()
		#self.server.toAnswer(to)
		self.server.logfile.flush()
		#print(to)

	def Update(self):
		self.UpdateSocket()
		self.UpdateDevices()


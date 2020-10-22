import Server
import DeviceAdapter

class Updater:

	def __init__(self):
		self.deviceAdapter = DeviceAdapter()
		self.server = Server()

	def UpdateDevices(self):
		pass

	def UpdateSocket(self):
		pass

	def Update(self):
		dThread = threading.Thread(target=UpdateDevices, daemon = true)
		sThread = threading.Thread(target=UpdateSocket, daemon = true)
		dThread.start()
		sThread.start()


import Server
import DeviceAdapter

class Updater:

	def __init__(self):
		self.deviceAdapter = DeviceAdapter()
		self.server = Server()

	def UpdateDevices(self):
		ExecuteCommand()
		getStates()#in command get state

	def UpdateSocket(self):
		server.GetRecievedData()
		for i in server.data:
			getCommand()
			deviceAdapter.AddCommand()
		for j in deviceAdapter.answers:
			server.sendAnswer(j)
		for client in server.clients:
			for device in deviceAdapter.devices:
				server.sendState(client, deviceAdapter.getLastState(device))

	def Update(self):
		dThread = threading.Thread(target=UpdateDevices, daemon = true)
		sThread = threading.Thread(target=UpdateSocket, daemon = true)
		dThread.start()
		sThread.start()


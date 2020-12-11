import Updater as upd
import time
import Server as srv

if __name__ == "__main__":
	try:

		f = open("config.cfg", "r")
		serverlog = open("logs/server.log", "w")
		port = int(f.readline().split('=')[1])
		code = f.readline().split('=')[1].strip()
		timeout = float(f.readline().split('=')[1])
		ticksTosend = int(f.readline().split('=')[1])
		server = srv.Server(port, code, timeout, serverlog)
		upd = upd.Updater(server)
		print("Started Succesfully!")
		while(1):
			upd.Update()
			time.sleep(1)
	except:
		print("End!", e)
	serverlog.close()
	f.close()
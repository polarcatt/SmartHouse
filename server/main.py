import Updater
import time

if __name__ == "__main__":
	upd = Updater()
	while(1):
		upd.Update()
		time.sleep(0.1)
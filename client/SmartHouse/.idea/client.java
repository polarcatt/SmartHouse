package SmartHouse;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.Socket;

class client {

    private DataOutputStream dos = null;
    private InputStream dis = null;
    int port = 11843;
    Socket mSocket = null;
    PrintWriter writer;
    boolean log = false;
    boolean con = false;

    public void Connect() {
	try {
	    mSocket = new Socket("localhost", port);
	    OutputStream output = mSocket.getOutputStream();
	    writer = new PrintWriter(output, true);
	    dos = new DataOutputStream(output);
	    dis = mSocket.getInputStream();

	} catch (Exception e) {
	    System.out.println(e.getMessage());
	    System.out.println("Ошибка при создании сокета");
	}
    }

    public void GetPacket() {
	byte[] buffer = new byte[1024];
	int read;
	String dataString = null;

	try {
	    if (dis.available() > 0)
		while (dis.available() > 0 && (read = dis.read(buffer)) > 0) {
		    dataString = new String(buffer, 0, read);
		    int count1 = 0;
		    int count2 = 0;
		    // Log.e(LOG_TAG, dataString);
		    for (int i = 0; i < dataString.length(); i++) {
			if (dataString.charAt(i) == '{')
			    count1++;
			if (dataString.charAt(i) == '}')
			    count2++;
		    }
		    if (count1 == count2 && count1 != 0 && count2 != 0) {
			System.out.println(dataString);
			ParsePacket(dataString);
			break;
		    } else
			System.out.println("Warning");
		}

	} catch (IOException e) {
	    System.out.println(e.getMessage());
	    System.out.println("Ошибка при чтении с сервера");
	}
	// System.out.println(dataString);
    }

    public void ParsePacket(String packet) {
	packet = packet.replace("{", "");
	packet = packet.replace("}", "");
	packet = packet.replace("\'", "");
	int index = packet.indexOf(",");
	if (packet.indexOf("status") != -1) {
	    packet = packet.substring(packet.indexOf("id"));
	    System.out.println(packet);
	}
	if (index != -1) {
	    String[] com = packet.split(",");
	    for (String t : com)
		System.out.println(t);
	} else {
	    String[] com = packet.split(":");
	    for (String t : com)
		System.out.println(t);
	}
    }

    public void SendCommand(int deviceNumber, String commandToDevice, String deviceName) {
	writer.println("{\'command\':{\'device\':\'" + deviceNumber + "\',\'command\':\'" + commandToDevice
		+ "\',\'name\':\'" + deviceName + "\'}}");
	// Log.e(LOG_TAG, "{\'command\':{\'device\':\'" + deviceNumber +
	// "\',\'command\':\'" + commandToDevice
	// + "\',\'name\':\'" + deviceName + "\'}}");
    }

    public void CheckPass(String pass) {
	writer.println("{\'pass\'" + ":" + "\'" + pass + "\'}");
	// Log.e(LOG_TAG, "{\'pass\'" + ":" + "\'" + pass + "\'}");
    }

    /*
     * final Handler handler = new Handler(); Timer timer = new Timer(false);
     * TimerTask timerTask = new TimerTask() {
     * 
     * @Override public void run() { handler.post(new Runnable() {
     * 
     * @Override public void run() {
     * 
     * } }); } }; timer.schedule(timerTask, 100, 100);
     */
    public void Close() {
	if (mSocket != null && !mSocket.isClosed()) {
	    try {
		mSocket.close();
		dos.close();
		dis.close();
	    } catch (IOException e) {
		System.out.println("Ошибка при закрытии сокета");
	    } finally {
		mSocket = null;
		dos = null;
		dis = null;
	    }
	}
    }
}

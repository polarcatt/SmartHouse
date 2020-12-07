import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

class Client {

	private static OutputStream output;
    private static InputStream input;
    private static DataOutputStream dos;
    private static DataInputStream dstream;
    private  int PORT = 11813;

	public static void Connect(String ip) {
		
        mConnect = new Second.Connection(ip, PORT);
        
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    mConnect.openConnection();
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {}
                    });
                    Log.i(LOG_TAG, "Соединение установлено");
                    Log.i(LOG_TAG, "(mConnect != null) = "
                            + (mConnect != null));
                    dos.writeBytes("Hello");
                } catch (Exception e) {
                    Log.i(LOG_TAG, e.getMessage());
                    mConnect = null;
                }
            }
        }).start();
    

    public void onCloseClick() {
        mConnect.closeConnection();
        Log.i(LOG_TAG, "Соединение закрыто");
    }

    	public static class Connection {
	        private Socket mSocket = null;
	        private String mHost = null;
	        private int mPort = 0;
	        private EditText textView2 = null;

	        public static final String LOG_TAG = "SOCKET";

	        public Connection(final String host, final int port) {
	            this.mHost = host;
	            this.mPort = port;
	        }

	        public void openConnection() throws Exception {
	            try {
	                mSocket = new Socket(mHost, mPort);
	                output = mSocket.getOutputStream();
	                input = mSocket.getInputStream();
	                dos = new DataOutputStream(output);
	                dstream = new DataInputStream(input);
	            } catch (IOException e) {
	                throw new Exception("Невозможно создать сокет: "
	                        + e.getMessage());
	            }
	        }

	        public void closeConnection() {
	            if (mSocket != null && !mSocket.isClosed()) {
	                try {
	                    mSocket.close();
	                    dos.close();
	                    input.close();
	                    output.close();
	                    dstream.close();
	                } catch (IOException e) {
	                    Log.i(LOG_TAG, "Ошибка при закрытии сокета :"
	                            + e.getMessage());
	                } finally {
	                    mSocket = null;
	                }
	            }
	            mSocket = null;
	        }

	        protected void finalize() throws Throwable {
	            super.finalize();
	            closeConnection();
	        }
    	}
	}
/*
	public static boolean CheckPass() {

	}

	public static void SendCommand() {

	}

	public static byte GetPacket() {

	}

	public static ParsePacket() {

	}

	public static void Close() {

	} */
}
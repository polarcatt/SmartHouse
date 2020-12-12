package com.example.smarthouse;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.util.Random;
import java.util.Timer;
import java.util.TimerTask;

import test.Client.Connection;

class Client {
    
    private static OutputStream output;
    private static InputStream input;
    private static DataOutputStream dos;
    private static DataInputStream dstream;
    private static Connection mConnect;
    private static int PORT = 11815;
    private static Socket mSocket = null;

    public void Connect(String ip) {
        
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    mSocket = new Socket(ip, PORT);
                    output = mSocket.getOutputStream();
                    input = mSocket.getInputStream();
                    dos = new DataOutputStream(output);
                    dstream = new DataInputStream(input);
                    //Log.i(LOG_TAG, "Соединение установлено");
                    //Log.i(LOG_TAG, "(mConnect != null) = "
                          //  + (mConnect != null));
                    dos.writeBytes("Hello");
                } catch (Exception e) {
                    //Log.i(LOG_TAG, e.getMessage());
                }
            }
        }).start();
    }
    
    public static void Close() {
        if (mSocket != null && !mSocket.isClosed()) {
                try {
                    mSocket.close();
                    dos.close();
                    input.close();
                    output.close();
                    dstream.close();
                } catch (IOException e) {
                    //Log.i(LOG_TAG, "Ошибка при закрытии сокета :"
                           // + e.getMessage());
                } finally {
                    mSocket = null;
                }
            }
            mSocket = null;
    } 

    public static boolean CheckPass(String pass) {
        dos.writeBytes(pass);

        if(dstream != null && dstream.available() > 0) {
            Log.i(LOG_TAG, "ЖДЕМ");

            byte[] messageByte = new byte[1000];
            String dataString = "";
            int bytesRead;

            while((bytesRead = dstream.read(messageByte)) > 0) 
            {
                dataString += new String(messageByte, 0, bytesRead);
            }

            ParsePacket(dataString);
        }   
        else return "";
    }

    public static ParsePacket(String packet) {
        
    }
/*
    

    public static void SendCommand(device, command) {

    }

    public static byte GetPacket() {

    }

    
    */
    
}
package com.liamcolangelo;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URI;

// Change nothing in this file except what comments clearly allow.
public class App {
    private WebSocketClient webSocketClient;
    private JFrame frame;
    // Components of JFram to be accesible by several parts of the program
    private JTextField text_field;
    // End of JFrame components

    public App() {
        frame = new JFrame("My GUI App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Create and add GUI components to the JFrame
        text_field = new JTextField("Hello, World!");
        frame.add(text_field, BorderLayout.CENTER);
        text_field.addActionListener(new TextListener());
        // End of GUI components


        try {
            webSocketClient = new WebSocketClient(new URI("ws://localhost:8000/")) {
                @Override
                public void onOpen(ServerHandshake handshakedata) {
                    System.out.println("Connected to server");
                }

                @Override
                public void onMessage(String message) {
                    System.out.println("Received message: " + message);
                    text_field.setText(message);
                }

                @Override
                public void onError(Exception ex) {
                    ex.printStackTrace();
                }

                @Override
                public void onClose(int code, String reason, boolean remote) {
                    System.out.println("Connection closed: " + reason);
                }
            };


            Thread webSocketThread = new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        webSocketClient.connect();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                }
            });
            webSocketThread.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void run() {
        // Set the size of JFrame (only change this)
        frame.setSize(400, 300);
        frame.setVisible(true);
    }

    public void sendMessage(String message)
    {
        if (webSocketClient != null && webSocketClient.isOpen()) {
            webSocketClient.send(message);
            System.out.println("Sent message: " + message);
        } else {
            System.out.println("WebSocket connection is not open");
        }
    }

    // Add event listeners here
    private class TextListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            sendMessage(text_field.getText());
        }
    }
    // End of event listeners

    public static void main(String[] args) {
        App app = new App();
        app.run();
    }
}

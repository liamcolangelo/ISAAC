package com.liamcolangelo;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.net.URI;

public class App {
    private WebSocketClient webSocketClient;
    private JFrame frame;
    private JTextField text_field;

    public App() {
        // Create and configure the JFrame
        frame = new JFrame("My GUI App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Create and add GUI components to the JFrame
        text_field = new JTextField("Hello, World!");
        frame.add(text_field, BorderLayout.CENTER);
        text_field.addActionListener(new TextListener());

        // Configure WebSocketClient and establish the connection
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

            // Start the WebSocketClient in a separate thread
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
        // Set the size and visibility of the JFrame
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

    private class TextListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            sendMessage(text_field.getText());
        }
    }

    public static void main(String[] args) {
        App app = new App();
        app.run();
    }
}

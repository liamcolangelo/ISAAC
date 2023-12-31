package com.liamcolangelo;
import org.java_websocket.client.WebSocketClient;
import org.java_websocket.handshake.ServerHandshake;
import javax.swing.*;
import javax.swing.event.*;
import java.awt.*;
import java.net.URI;

// Change nothing in this file except what comments clearly allow.
public class App {
    private WebSocketClient webSocketClient;
    private JFrame frame;
    // Components of JFram to be accesible by several parts of the program
    private JTextArea ISAAC_field;
    private JLabel weather;
    // End of JFrame components

    public App() {
        frame = new JFrame("My GUI App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(2,1,4,4));

        // Create and add GUI components to the JFrame
        ISAAC_field = new JTextArea("Hello, World!", 4, 20); // Center this at some point
        ISAAC_field.setLineWrap(true);
        ISAAC_field.setWrapStyleWord(true);
        JScrollPane scroll_pane = new JScrollPane(ISAAC_field);
        frame.add(scroll_pane);
        ISAAC_field.getDocument().addDocumentListener(new ISAAC_listener());
        weather = new JLabel("Weather", JLabel.CENTER);
        weather.setFont(new Font("Arial", Font.PLAIN, 30));
        frame.add(weather);
        // End of GUI components


        try {
            webSocketClient = new WebSocketClient(new URI("ws://localhost:8000/")) {
                @Override
                public void onOpen(ServerHandshake handshakedata) {
                    System.out.println("Connected to server");
                }

                @Override
                public void onMessage(String message) {
                    int type = Integer.parseInt(message.substring(0,4));
                    message = message.substring(5);
                    if (type == 0000) {
                        System.out.println("Debug: " + message);
                    } else if (type == 0001) {
                        // Process information here (not displayed)
                    } else if (type == 0002) {
                        ISAAC_field.setText(message);
                    } else if (type == 0003) {
                        weather.setText(message);
                    } else {
                        System.out.println("Incorrect message format");
                    }
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
    /*
    private class ISAACFieldListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            sendMessage("0200:" + ISAAC_field.getText());
        }
    }
    */

    private class ISAAC_listener implements DocumentListener {
        public void insertUpdate(DocumentEvent e) {
            updateLog(e, "inserted into");
        }

        public void removeUpdate(DocumentEvent e) {
            // updateLog(e, "removed from");
        }

        public void changedUpdate(DocumentEvent e) {
            // Don't worry about this
        }

        public void updateLog(DocumentEvent e, String action) {
            int length = ISAAC_field.getText().length();
            if (ISAAC_field.getText().charAt(length - 1) == '\n') {
                sendMessage("0200:" + ISAAC_field.getText().substring(0, length - 1));
            }
        }
    }
    // End of event listeners

    public static void main(String[] args) {
        App app = new App();
        app.run();
    }
}

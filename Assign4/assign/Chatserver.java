import java.io.*;
import java.net.*;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.concurrent.*;

public class Chatserver {
    private static final int PORT = 8082;
    private static final SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");
    private static final Map<Socket, PrintWriter> clients = new ConcurrentHashMap<>();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Chat server is ready to receive connections.");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                clients.put(clientSocket, out);
                new ClientHandler(clientSocket, out).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static void broadcast(String message) {
        synchronized (clients) {
            for (PrintWriter client : clients.values()) {
                client.println(message);
            }
        }
    }

    static class ClientHandler extends Thread {
        private Socket clientSocket;
        private PrintWriter out;
        private String name;

        public ClientHandler(Socket socket, PrintWriter writer) {
            clientSocket = socket;
            out = writer;
        }

        public void run() {
            try (BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()))) {
                out.println("Enter your name:");
                name = in.readLine();
                broadcast(name + " has joined the chat.");

                String message;
                while ((message = in.readLine()) != null) {
                    String timestamp = dateFormat.format(new Date());
                    String formattedMessage = timestamp + " " + name + ": " + message;
                    broadcast(formattedMessage);

                    if (message.equalsIgnoreCase("exit")) {
                        System.out.println(name + " has left the chat."); 
                        break;
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                clients.remove(clientSocket);
                System.out.println(name + " has left the chat."); 
                try {
                    clientSocket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

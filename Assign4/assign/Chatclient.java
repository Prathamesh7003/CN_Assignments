import java.io.*;
import java.net.*;
import java.text.SimpleDateFormat;
import java.util.Scanner;
import java.util.Date;

public class Chatclient {
    private static final String SERVER_ADDRESS = "127.0.0.1";
    private static final int SERVER_PORT = 8082;
    private static final SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");

    public static void main(String[] args) {
        try (Socket socket = new Socket(SERVER_ADDRESS, SERVER_PORT);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             Scanner scanner = new Scanner(System.in)) {
            System.out.println("Connected to the chat server.");
            String serverMessage;

            while (true) {
                serverMessage = in.readLine();
                if (serverMessage == null) {
                    break;
                }
                System.out.println(serverMessage);

                String userInput = scanner.nextLine();
                String timestamp = dateFormat.format(new Date());
                out.println(userInput);

                if (userInput.equalsIgnoreCase("exit")) {
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

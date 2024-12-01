package ia;

import org.json.JSONObject;
import org.json.JSONArray;

import java.io.*;
import java.net.*;
import java.util.ArrayList;

public class Server {

    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(12345);
        System.out.println("Servidor Java iniciado. Esperando conexiones...");

        while (true) {
            try (Socket clientSocket = serverSocket.accept();
                    BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                    PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                System.out.println("Cliente conectado: " + clientSocket.getInetAddress());

                // Read the entire input
                StringBuilder requestBuilder = new StringBuilder();
                int ch;
                while ((ch = in.read()) != -1) {
                    requestBuilder.append((char) ch);
                    // Break if we've received a complete JSON (you might need to adjust this logic)
                    if (requestBuilder.toString().trim().endsWith("}")) {
                        break;
                    }
                }

                String inputLine = requestBuilder.toString().trim();
                if (!inputLine.isEmpty()) {
                    procesarSolicitud(inputLine, out);
                }

            } catch (IOException e) {
                System.err.println("Error al manejar la conexión del cliente: " + e.getMessage());
            }
        }
    }

    private static void procesarSolicitud(String inputLine, PrintWriter out) {
        try {
            System.out.println("Datos recibidos del cliente: " + inputLine);

            JSONObject request = new JSONObject(inputLine);
            String origen = request.getString("origen");
            String linea_origen = origen.substring(origen.length() - 1);
            origen = origen.substring(0, origen.length() - 2);
            String destino = request.getString("destino");
            destino = destino.substring(0, destino.length() - 2);

            System.out.println("Calculando ruta desde " + origen + " (" + linea_origen + ") hasta " + destino);

            Main main = new Main();
            ArrayList<String> ruta = main.AStar(Grafo.getInstance(), origen, linea_origen, destino);
            if (ruta == null) {
                enviarError(out, "No se pudo encontrar una ruta.");
                return;
            }

            double tiempo = main.calcularTiempo(ruta);

            JSONObject response = new JSONObject();
            response.put("ruta", new JSONArray(ruta));
            response.put("tiempo", tiempo);

            enviarRespuesta(out, response.toString());

        } catch (Exception e) {
            System.err.println("Error al procesar la solicitud: " + e.getMessage());
            e.printStackTrace();
            enviarError(out, "Error al procesar la solicitud: " + e.getMessage());
        }
    }

    private static void enviarRespuesta(PrintWriter out, String respuesta) {
        out.println(respuesta);
        System.out.println("Respuesta enviada al cliente: " + respuesta);
    }

    private static void enviarError(PrintWriter out, String mensajeError) {
        JSONObject errorResponse = new JSONObject();
        try {
            errorResponse.put("error", mensajeError);
        } catch (Exception jsonEx) { // para ser ultra seguros que algo no explote
            System.err.println("Error creando JSON de error: " + jsonEx.getMessage());
            out.println("{\"error\": \"Error interno del servidor\"}");
            return;
        }

        out.println(errorResponse.toString());
        System.err.println("Error enviado al cliente: " + errorResponse.toString());
    }
}

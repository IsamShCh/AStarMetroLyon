package ia;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.PriorityQueue;

import org.json.JSONObject;
import org.json.JSONArray;

public class Main {

	// Función para calcular el tiempo total de la ruta
	public double calcularTiempo(ArrayList<String> ruta) {
		double tiempo_total = 0;
		if (ruta != null) {
			for (int i = 0; i < ruta.size() - 1; i++) {

				String estacion1 = ruta.get(i);
				String estacion2 = ruta.get(i + 1);

				Vertice v1 = Grafo.getInstance().devuelveVertice(estacion1.substring(0, estacion1.length() - 2),
						estacion1.substring(estacion1.length() - 1));
				Vertice v2 = Grafo.getInstance().devuelveVertice(estacion2.substring(0, estacion2.length() - 2),
						estacion2.substring(estacion2.length() - 1));

				// encontrar la arista que conecta v1 y v2
				for (Aristas arista : v1.getAristas()) {
					if (arista.getV1() == v2 || arista.getV2() == v2) {
						tiempo_total += arista.getPeso();
						break;
					}
				}

			}
		}

		return tiempo_total;
	}

	public static void main(String[] args) throws Exception {
		// El main ahora solo inicia el servidor
		// Server.main(args);

	}

	public ArrayList<String> AStar(Grafo grafo, String inicio, String linea, String destino) {

		HashSet<Vertice> cerrados = new HashSet<Vertice>();

		Vertice init = grafo.devuelveVertice(inicio, linea);
		Coordenadas mapa = new Coordenadas();
		PriorityQueue<Vertice> abiertos = new PriorityQueue<Vertice>(20, new Comparator<Vertice>() {
			public int compare(Vertice i, Vertice j) {
				if (i.f > j.f) {
					return 1;
				} else if (i.f < j.f) {
					return -1;
				} else {
					return 0;
				}
			}
		});

		init.f = mapa.HaversineFormula(inicio, destino);
		init.g = 0;
		abiertos.add(init);
		Vertice actual;

		while (!abiertos.isEmpty()) {
			actual = abiertos.peek();
			if (actual.getNombre().equals(destino)) {
				Vertice temp = actual;

				ArrayList<Vertice> lista = new ArrayList<Vertice>();

				while (temp != null) {
					lista.add(0, temp);
					temp = temp.padre;
				}

				ArrayList<String> lista_nombres = new ArrayList<String>();
				for (Vertice x : lista) {
					lista_nombres.add(x.getNombre() + " " + x.getLinea());
				}

				return lista_nombres; // que devuelva la cadena

			}
			cerrados.add(abiertos.poll());

			for (Aristas AVecinos : actual.getAristas()) {
				Vertice vecino = AVecinos.getVX(actual);
				if (cerrados.contains(vecino)) {
					continue;
				}
				double costo_G = actual.g + AVecinos.getPeso();
				if (costo_G < vecino.g) {
					vecino.g = costo_G;
					vecino.f = mapa.HaversineFormula(destino, vecino.getNombre()) + costo_G;
					vecino.padre = actual;
					if (!abiertos.contains(vecino))
						abiertos.add(vecino);
				}
			}
		}
		return null;

	}

}

package ia;

import java.util.LinkedList;

public class Grafo {
	public LinkedList<Aristas> aristas;
	public LinkedList<Vertice> vertice;

	private static Grafo instance = null;

	private Grafo() {
		aristas = new LinkedList<>();
		vertice = new LinkedList<>();

		// Inicialización del grafo (lo que antes estaba en el main)
		ponerVertice("Vaulx-en-Velin La Soie", "A");
		ponerVertice("Vaulx-en-Velin La Soie", "A");
		ponerVertice("Laurent Bonnevay Atroballe", "A");
		ponerVertice("Cusset", "A");
		ponerVertice("Flachet", "A");
		ponerVertice("Gratte-Ciel", "A");
		ponerVertice("Republique Villeurbanne", "A");
		ponerVertice("Charpennes Charles Hernu", "A");
		ponerVertice("Massena", "A");
		ponerVertice("Foch", "A");
		ponerVertice("Hotel de Ville Louis Pradel", "A");
		ponerVertice("Cordeliers", "A");
		ponerVertice("Bellecour", "A");
		ponerVertice("Ampere Victor Hugo", "A");
		ponerVertice("Perrache", "A");
		ponerVertice("Oullins Gare", "B");
		ponerVertice("Stade de Gerland", "B");
		ponerVertice("Debourg", "B");
		ponerVertice("Place Jean Jaures", "B");
		ponerVertice("Jean Mace", "B");
		ponerVertice("Saxe Gambetta", "B");
		ponerVertice("Place Guichard Bourse de Travail", "B");
		ponerVertice("Gare Part-Dieu Vivier Merle", "B");
		ponerVertice("Brotteaux", "B");
		ponerVertice("Charpennes Charles Hernu", "B");
		ponerVertice("Cuire", "C");
		ponerVertice("Henon", "C");
		ponerVertice("Croix-Rousse", "C");
		ponerVertice("Croix-Paquet", "C");
		ponerVertice("Hotel de Ville Louis Pradel", "C");
		ponerVertice("Gare de Vaise", "D");
		ponerVertice("Valmy", "D");
		ponerVertice("Gorge de Loup", "D");
		ponerVertice("Vieux Lyon Cathedrale St Jean", "D");
		ponerVertice("Bellecour", "D");
		ponerVertice("Guillotiere", "D");
		ponerVertice("Saxe Gambetta", "D");
		ponerVertice("Garibaldi", "D");
		ponerVertice("Sans-Souci", "D");
		ponerVertice("Monsplaisir-Lumiere", "D");
		ponerVertice("Grange Blanche", "D");
		ponerVertice("Laennec", "D");
		ponerVertice("Mermoz Pincel", "D");
		ponerVertice("Parilly", "D");
		ponerVertice("Gare de Venissieux", "D");

		try {

			ponerAristaEntre("Vaulx-en-Velin La Soie", "Laurent Bonnevay Atroballe", "A", "A", 2);
			ponerAristaEntre("Laurent Bonnevay Atroballe", "Cusset", "A", "A", 1);
			ponerAristaEntre("Cusset", "Flachet", "A", "A", 2);
			ponerAristaEntre("Flachet", "Gratte-Ciel", "A", "A", 1);
			ponerAristaEntre("Gratte-Ciel", "Republique Villeurbanne", "A", "A", 1);
			ponerAristaEntre("Republique Villeurbanne", "Charpennes Charles Hernu", "A", "A", 2);
			ponerAristaEntre("Charpennes Charles Hernu", "Massena", "A", "A", 1);
			ponerAristaEntre("Massena", "Foch", "A", "A", 1);
			ponerAristaEntre("Foch", "Hotel de Ville Louis Pradel", "A", "A", 1);
			ponerAristaEntre("Hotel de Ville Louis Pradel", "Cordeliers", "A", "A", 1);
			ponerAristaEntre("Cordeliers", "Bellecour", "A", "A", 2);
			ponerAristaEntre("Bellecour", "Ampere Victor Hugo", "A", "A", 1);
			ponerAristaEntre("Ampere Victor Hugo", "Perrache", "A", "A", 1);

			ponerAristaEntre("Oullins Gare", "Stade de Gerland", "B", "B", 4);
			ponerAristaEntre("Stade de Gerland", "Debourg", "B", "B", 1);
			ponerAristaEntre("Debourg", "Place Jean Jaures", "B", "B", 2);
			ponerAristaEntre("Place Jean Jaures", "Jean Mace", "B", "B", 1);
			ponerAristaEntre("Jean Mace", "Saxe Gambetta", "B", "B", 2);
			ponerAristaEntre("Saxe Gambetta", "Place Guichard Bourse de Travail", "B", "B", 1);
			ponerAristaEntre("Place Guichard Bourse de Travail", "Gare Part-Dieu Vivier Merle", "B", "B", 2);
			ponerAristaEntre("Gare Part-Dieu Vivier Merle", "Brotteaux", "B", "B", 1);
			ponerAristaEntre("Brotteaux", "Charpennes Charles Hernu", "B", "B", 2);

			ponerAristaEntre("Cuire", "Henon", "C", "C", 3);
			ponerAristaEntre("Henon", "Croix-Rousse", "C", "C", 2);
			ponerAristaEntre("Croix-Rousse", "Croix-Paquet", "C", "C", 2);
			ponerAristaEntre("Croix-Paquet", "Hotel de Ville Louis Pradel", "C", "C", 2);

			ponerAristaEntre("Gare de Vaise", "Valmy", "D", "D", 2);
			ponerAristaEntre("Valmy", "Gorge de Loup", "D", "D", 2);
			ponerAristaEntre("Gorge de Loup", "Vieux Lyon Cathedrale St Jean", "D", "D", 2);
			ponerAristaEntre("Vieux Lyon Cathedrale St Jean", "Bellecour", "D", "D", 1);
			ponerAristaEntre("Bellecour", "Guillotiere", "D", "D", 1);
			ponerAristaEntre("Guillotiere", "Saxe Gambetta", "D", "D", 1);
			ponerAristaEntre("Saxe Gambetta", "Garibaldi", "D", "D", 1);
			ponerAristaEntre("Garibaldi", "Sans-Souci", "D", "D", 1);
			ponerAristaEntre("Sans-Souci", "Monsplaisir-Lumiere", "D", "D", 1);
			ponerAristaEntre("Monsplaisir-Lumiere", "Grange Blanche", "D", "D", 1);
			ponerAristaEntre("Grange Blanche", "Laennec", "D", "D", 1);
			ponerAristaEntre("Laennec", "Mermoz Pincel", "D", "D", 1);
			ponerAristaEntre("Mermoz Pincel", "Parilly", "D", "D", 2);
			ponerAristaEntre("Parilly", "Gare de Venissieux", "D", "D", 3);

			// Correspondencia

			ponerAristaEntre("Bellecour", "Bellecour", "D", "A", 2);
			ponerAristaEntre("Saxe Gambetta", "Saxe Gambetta", "D", "B", 1);
			ponerAristaEntre("Hotel de Ville Louis Pradel", "Hotel de Ville Louis Pradel", "C", "A", 1);
			ponerAristaEntre("Charpennes Charles Hernu", "Charpennes Charles Hernu", "A", "B", 2);

		} catch (Exception e) {
			System.err.println("Error al crear el grafo: " + e.getMessage());
		}
		System.out.println("Grafo crado");
	}

	public static Grafo getInstance() {
		if (instance == null) {
			instance = new Grafo();
			System.out.println("NEW GRAFO");
		}
		return instance;
	}

	// Métodos para crear el grafo
	public void ponerVertice(String nombre, String linea) {
		Vertice v = new Vertice(nombre, linea);
		vertice.add(v);
	}

	public void ponerAristaEntre(String name1, String name2, String linea1, String linea2, float peso)
			throws Exception {
		if (!existeVertice(name1) || !existeVertice(name2)) {
			throw new Exception("Algunos de los vértices no existen");
		} else {
			Vertice v1 = devuelveVertice(name1, linea1);
			Vertice v2 = devuelveVertice(name2, linea2);
			Aristas arista = new Aristas(v1, v2, peso);
			aristas.add(arista);
			int n1 = vertice.indexOf(v1);
			int n2 = vertice.indexOf(v2);
			vertice.get(n1).getAristas().add(arista);
			vertice.get(n2).getAristas().add(arista);
		}
	}

	// Getters, Setters y toString
	public LinkedList<Aristas> getAristas() {
		return aristas;
	}

	public void setAristas(LinkedList<Aristas> aristas) {
		this.aristas = aristas;
	}

	public LinkedList<Vertice> getVertices() {
		return vertice;
	}

	public void setVertices(LinkedList<Vertice> vertice) {
		this.vertice = vertice;
	}

	@Override
	public String toString() {
		return "Grafo [aristas=" + aristas + ", vertice=" + vertice + "]";
	}

	// Métodos Privados
	private boolean existeVertice(String name) {
		for (Vertice v : vertice) {
			if (v.getNombre().equals(name)) {
				return true;
			}
		}
		return false;
	}

	public Vertice devuelveVertice(String name, String linea) {
		for (Vertice v : vertice) {
			if (v.getNombre().equals(name) && v.getLinea().equals(linea)) {
				return v;
			}
		}
		return null;
	}
}
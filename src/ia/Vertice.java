package ia;

import java.util.LinkedList;

public class Vertice {
	private String nombre;
	private LinkedList<Aristas> aristas;
	private String linea;
	
	
	//////////
	public double g = 999999999;
	public double f = 999999999; // hacerlo mas piola
	//////////
	public Vertice padre;
	
	
	public Vertice(String nombre,LinkedList<Aristas> aristas,String linea) {
		this.nombre=nombre;
		this.aristas=aristas;
		this.setLinea(linea);
		this.padre = null;
	}
	
	public Vertice getPadre()
	{
		return padre;
	}
	
	public Vertice(String nombre, String linea) {
		this.nombre=nombre;
		this.aristas=new LinkedList<>();
		this.setLinea(linea);
	}
	
	public void ponerArista(Aristas arista) {
		aristas.add(arista);
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public LinkedList<Aristas> getAristas() {
		return aristas;
	}

	public void setAristas(LinkedList<Aristas> aristas) {
		this.aristas = aristas;
	}

	@Override
	public String toString() {
		//return "Vertices [nombre=" + nombre + ", aristas=" + aristas + "]";
		return "Nombre: " + nombre + ", g= " + g + ", f= " + f;
	}

	public String getLinea() {
		return linea;
	}

	public void setLinea(String linea) {
		this.linea = linea;
	}
	
	public Aristas getAristaQueContiene(Vertice padre)
	{
		for (Aristas ar : aristas)
		{
			if (ar.getV1() == padre || ar.getV2() == padre)
				return ar;
		}
		return null;
	}
	
}

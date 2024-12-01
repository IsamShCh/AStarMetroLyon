package ia;

public class Aristas {
	private Vertice v1;
	private Vertice v2;
	private float peso;
	
	public Aristas(Vertice v1, Vertice v2, float peso) {
		this.v1 = v1;
		this.v2 = v2;
		this.peso = peso;
	}
	
	public Vertice getV1() {
		return v1;
	}

	public void setV1(Vertice v1) {
		this.v1 = v1;
	}

	public Vertice getV2() {
		return v2;
	}

	public void setV2(Vertice v2) {
		this.v2 = v2;
	}

	public float getPeso() {
		return peso;
	}

	public void setPeso(float peso) {
		this.peso = peso;
	}
	
	public Vertice getVX(Vertice vert)
	{
		if(vert == v1)
		{
			
			return v2;
		}
		else
		{
			
			return v1;
		}
		
	}
	
	@Override
	public String toString() {
		return v1.getNombre() + "-----"+peso+"-----" + v2.getNombre();
	}

	
}

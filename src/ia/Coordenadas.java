package ia;

import java.util.Hashtable;
import java.util.Map;

public class Coordenadas {
	public Map<String,Coordenada> coordenadas;
	
	public Coordenadas()
	{
		initCoordenadas();
		
	}
	
	public void initCoordenadas() {

		coordenadas = new Hashtable<String,Coordenada>();
		coordenadas.put("Vaulx-en-Velin La Soie", new Coordenada(45.761762868575104, 4.922073331123908));
		coordenadas.put("Laurent Bonnevay Atroballe",new Coordenada(45.76493198887359,4.908961283699688));
		coordenadas.put("Cusset",new Coordenada(45.7659550151363,4.900150448113281));
		coordenadas.put("Flachet",new Coordenada(45.76764645011455, 4.889936596136291));
		coordenadas.put("Gratte-Ciel",new Coordenada(45.76897860618024,4.88255515692166));
		coordenadas.put("Republique Villeurbanne",new Coordenada(45.77090942759724,4.873777627975983));
		coordenadas.put("Charpennes Charles Hernu",new Coordenada(45.77090942759724,4.873777627975983));
		coordenadas.put("Massena",new Coordenada(45.76962970460007,4.853005260061035));
		coordenadas.put("Foch",new Coordenada(45.76903567115259,4.844168722460625));
		coordenadas.put("Hotel de Ville Louis Pradel",new Coordenada(45.7676900606498,4.836309869931915));
		coordenadas.put("Cordeliers",new Coordenada(45.7636769229107,4.83573585731864));
		coordenadas.put("Bellecour",new Coordenada(45.75816795244077,4.833697378467326));
		coordenadas.put("Ampere Victor Hugo",new Coordenada(45.75321240831274,4.829191267331534));
		coordenadas.put("Perrache",new Coordenada(45.749678881564726,4.8271313308060115));
		coordenadas.put("Oullins Gare",new Coordenada(45.717186099582534, 4.814723126702776));
		coordenadas.put("Stade de Gerland",new Coordenada(45.727252451436335, 4.830777302500439));
		coordenadas.put("Debourg",new Coordenada(45.73149157959042, 4.834511661183965));
		coordenadas.put("Place Jean Jaures",new Coordenada(45.7383186262974, 4.837528271938231));
		coordenadas.put("Jean Mace",new Coordenada(45.74605919792454, 4.842436705345269));
		coordenadas.put("Saxe Gambetta",new Coordenada(45.75418186324806, 4.847102129757356));
		coordenadas.put("Place Guichard Bourse de Travail",new Coordenada(45.75962779871013, 4.847693007768899));
		coordenadas.put("Gare Part-Dieu Vivier Merle",new Coordenada(45.76193765671962, 4.8577916866140205));
		coordenadas.put("Brotteaux",new Coordenada(45.767131920260255, 4.859293723684989));
		coordenadas.put("Cuire",new Coordenada(45.78618455720426, 4.833389920301244));
		coordenadas.put("Henon",new Coordenada(45.77474309720903, 4.8319224701525565));
		coordenadas.put("Croix-Rousse", new Coordenada(45.77794737917245, 4.823276996613431));
		coordenadas.put("Croix-Paquet",new Coordenada(45.7713122504698, 4.836352785267795));
		coordenadas.put("Gare de Vaise",new Coordenada(45.78048231058625, 4.805055458123392));
		coordenadas.put("Valmy",new Coordenada(45.77487227929711, 4.805563912679871));
		coordenadas.put("Gorge de Loup",new Coordenada(45.766169182520045, 4.805121319535386));
		coordenadas.put("Vieux Lyon Cathedrale St Jean", new Coordenada(45.75995511695618, 4.825753754126562));
		coordenadas.put("Guillotiere",new Coordenada(45.75559305426432, 4.8422499204183405));
		coordenadas.put("Garibaldi",new Coordenada(45.75175943799527, 4.854052378504019));
		coordenadas.put("Sans-Souci",new Coordenada(45.74816275723573, 4.864401599917525));
		coordenadas.put("Monsplaisir-Lumiere",new Coordenada(45.74579650385851, 4.871320498541155));
		coordenadas.put("Grange Blanche",new Coordenada(45.74319564346226, 4.878856412759967));
		coordenadas.put("Laennec",new Coordenada(45.73850854872427, 4.886461191790388));
		coordenadas.put("Mermoz Pincel",new Coordenada(45.730555650420236, 4.887139724364558));
		coordenadas.put("Parilly",new Coordenada(45.71971412243474, 4.887597977015012));
		coordenadas.put("Gare de Venissieux",new Coordenada(45.705790679450935, 4.887839543809754));
	
	}
	
	public Coordenada getCoordenadas(String nombre)
	{
		return coordenadas.get(nombre);
	}
	
	
	public double HaversineFormula(String estacion1,String estacion2) {
		double earthRadius = 6371; // km
		double lat1 = Math.toRadians(coordenadas.get(estacion1).getLatitud());
		double lon1 = Math.toRadians(coordenadas.get(estacion1).getLongitud());
		double lat2 = Math.toRadians(coordenadas.get(estacion2).getLatitud());
		double lon2 = Math.toRadians(coordenadas.get(estacion2).getLongitud());

		double dlon = (lon2 - lon1);
		double dlat = (lat2 - lat1);

		double sinlat = Math.sin(dlat / 2);
		double sinlon = Math.sin(dlon / 2);

		double a = (sinlat * sinlat) + Math.cos(lat1)*Math.cos(lat2)*(sinlon*sinlon);
		double c = 2 * Math.asin (Math.min(1.0, Math.sqrt(a)));

		double distanceInMeters = earthRadius * c * 1000;
		return distanceInMeters/1000;
	}
	
	static class Coordenada{
		
		double latitud;
		double longitud;
		
		public Coordenada(double latitud, double longitud) {
			this.latitud=latitud;
			this.longitud=longitud;
		}

		public double getLatitud() {
			return latitud;
		}

		public void setLatitud(float latitud) {
			this.latitud = latitud;
		}

		public double getLongitud() {
			return longitud;
		}

		public void setLongitud(float longitud) {
			this.longitud = longitud;
		}
		
	}
}

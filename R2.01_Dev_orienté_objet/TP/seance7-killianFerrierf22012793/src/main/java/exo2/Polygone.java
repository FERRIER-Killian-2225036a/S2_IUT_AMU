package exo2;

public class Polygone extends FormeGeometrique {
	protected int[] longCotes;
	
	public Polygone(int nbCotes) {
		super("Polygone");
		longCotes = new int[nbCotes];
	}
	
	@Override
	public double getPerimetre() {
		double perimetre = 0;
		for (int i = 0; i < longCotes.length; i++) {
			perimetre += longCotes[i];
		}
		return perimetre;
	}

}

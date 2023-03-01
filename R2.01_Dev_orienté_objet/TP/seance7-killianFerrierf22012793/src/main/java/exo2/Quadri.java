package exo2;

public class Quadri extends Polygone {
	
	public Quadri(int coteUn, int coteDeux, int coteTrois, int coteQuatre) {
		super(4);
		longCotes[0] = coteUn;
		longCotes[1] = coteDeux;
		longCotes[2] = coteTrois;
		longCotes[3] = coteQuatre;
		nom = "Quadrilatere";
	}

}

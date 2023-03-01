package exo2;

public class Triangle extends Polygone {

	public Triangle(int coteUn, int coteDeux, int coteTrois) {
		super(3);
		longCotes[0] = coteUn;
		longCotes[1] = coteDeux;
		longCotes[2] = coteTrois;
		nom = "Triangle";
	}

}

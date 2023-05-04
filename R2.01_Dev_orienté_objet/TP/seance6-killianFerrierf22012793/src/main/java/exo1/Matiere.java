package exo1;

public class Matiere {
	private String nomMatiere;
	private int coeficient;
	
	public Matiere(String nomMatiere, int coeficient) {
		this.nomMatiere = nomMatiere;
		this.coeficient = coeficient;
	}
	
	public String getNomMatiere() {
		return nomMatiere;
	}
	public int getCoeficient() {
		return coeficient;
	}
}

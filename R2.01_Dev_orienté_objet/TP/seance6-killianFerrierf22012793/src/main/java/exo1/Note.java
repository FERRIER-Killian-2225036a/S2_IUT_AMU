package exo1;

public class Note {
	int valeur;
	String type;
	Matiere matiere;
	
	public Note(int valeur, String type, Matiere matiere) {
		this.valeur = valeur;
		this.type = type;
		this.matiere = matiere;
	}
	
	public int getValeur() {
		return valeur;
	}
	public String getType() {
		return type;
	}
	public Matiere getMatiere() {
		return matiere;
	}
	
}

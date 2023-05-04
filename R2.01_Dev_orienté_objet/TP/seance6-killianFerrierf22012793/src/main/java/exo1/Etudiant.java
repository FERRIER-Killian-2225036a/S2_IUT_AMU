package exo1;

public class Etudiant {
	private String nom;
	private int annee;
	private Note[] note;
	
	//Constructor
	public Etudiant(String nom, int annee, Note[] note) {
		this.nom = nom;
		this.annee = annee;
		this.note = note;
	}
	
	//Getter
	public String getNom() {
		return nom;
	}
	public int getAnnee() {
		return annee;
	}
	public Note[] getNotes() {
		return note;
	}
}

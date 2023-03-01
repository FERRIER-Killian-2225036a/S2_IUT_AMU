package exo1;

public class Professeur {
	private String nomProf;
	private Matiere matiere;
	private Note note;
	
	public Professeur(String nomProf, Matiere matiere, Note note) {
		this.nomProf = nomProf;
		this.matiere = matiere;
		this.note = note;
	}
	
	public String getNomProf() {
		return nomProf;
	}
	public Matiere getMatiere() {
		return matiere;
	}
	public Note getNote() {
		return note;
	}
}

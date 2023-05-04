package exo1;

public class UseEtudiant {

	public static void main(String[] args) {
		Matiere math = new Matiere("Math", 5);
		Matiere DOO = new Matiere("DOO", 3);
		
		Note note1 = new Note(12, "TD", math);
		Note note2 = new Note(14, "TD", DOO);
		Note[] tabNotes = {note1,note2};
		
		Professeur Gaetan = new Professeur("Mme.Gaetan", math, note1);
		Professeur Prost = new Professeur("Mr.Prost", DOO, note2);
		Professeur Casali = new Professeur("Mr.Casali", null, null);
		
		Etudiant Killian = new Etudiant("Killian", 2023, tabNotes);
		
		System.out.printf("Stats matiere math: %s %d\n", math.getNomMatiere(), math.getCoeficient());
		
		System.out.printf("Stats matiere DOO: %s %d\n", DOO.getNomMatiere(), DOO.getCoeficient());
		
		System.out.printf("Stats note1: %d %s ", note1.getValeur(), note1.getType());
		System.out.println(note1.getMatiere());
		
		System.out.println(tabNotes);
		
		System.out.print("Stats prof Gaetan: ");
		System.out.print(Gaetan.getNomProf()+" ");
		System.out.print(Gaetan.getMatiere()+" ");
		System.out.println(Gaetan.getNote()+" ");
		System.out.print("Stats prof Prost: ");
		System.out.print(Prost.getNomProf()+" ");
		System.out.print(Prost.getMatiere()+" ");
		System.out.println(Prost.getNote()+" ");
		System.out.print("Stats prof Casali: ");
		System.out.print(Casali.getNomProf()+" ");
		System.out.print(Casali.getMatiere()+" ");
		System.out.println(Casali.getNote()+" ");
		
		System.out.print("Stats etu Killian: ");
		System.out.print(Killian.getNom()+" ");
		System.out.print(Killian.getAnnee()+" ");
		System.out.println(Killian.getNotes()+" ");
		
		
		
	}

}

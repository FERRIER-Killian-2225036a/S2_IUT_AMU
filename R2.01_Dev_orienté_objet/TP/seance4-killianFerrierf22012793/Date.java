package fr.killian.date;

public class Date {
	private int jour;
	private int mois;
	private int annee;
	
	//Constructor
	public Date() {
		this.jour = 1;
		this.mois = 1;
		this.annee =1;
	}
	public Date(int jour, int mois, int annee) {
		this.jour = jour;
		this.mois = mois;
		this.annee = annee;
	}
	
	//Getter
	public int getJour() {
		return jour;
	}
	public int getMois() {
		return mois;
	}
	public int getAnnee() {
		return annee;
	}
	
	//Setter
	public void setJour(int jour) {
		this.jour = jour;
	}
	public void setMois(int mois) {
		this.mois = mois;
	}
	public void setAnnee(int annee) {
		this.annee = annee;
	}
	
	public void prochainJour() {
		if(jour != 31 && mois != 12) {
			jour += 1;
		}
		else if(jour == 31 && mois != 12) {
			jour = 1;
			mois += 1;
		}
		else if(jour == 31 && mois == 12) {
			jour = 1;
			mois = 1;
			annee += 1;
		}
		System.out.printf("Jour : %d, Mois : %d, Année : %d\n",jour,mois,annee);
	}

}

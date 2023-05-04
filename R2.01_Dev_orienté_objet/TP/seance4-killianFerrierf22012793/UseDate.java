package fr.killian.date;

public class UseDate {

	public static void main(String[] args) {
		Date date = new Date();
		date.prochainJour();	
		date.setJour(31);
		date.prochainJour();
		date.setJour(31);
		date.setMois(12);
		date.prochainJour();
	}

}

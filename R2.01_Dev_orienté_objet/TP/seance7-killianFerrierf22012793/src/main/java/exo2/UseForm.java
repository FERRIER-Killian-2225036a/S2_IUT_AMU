package exo2;

public class UseForm {

	public static void main(String[] args) {
//		Cercle cercle = new Cercle(3);
//		System.out.println("Le perimetre du cercle est de : " + cercle.getPerimetre());
//		Quadri quadri = new Quadri(4, 5, 6, 7);
//		System.out.println("Le perimetre du quadri est de : " + quadri.getPerimetre());
//		Triangle triangle = new Triangle(4, 5, 6);
//		System.out.println("Le perimetre du triangle est de : " + triangle.getPerimetre());
//		Rectangle rectangle = new Rectangle(4, 5);
//		System.out.println("Le perimetre du rectangle est de : " + rectangle.getPerimetre());
//		Carre carre = new Carre(4);
//		System.out.println("Le perimetre du carre est de : " + carre.getPerimetre());
		
		FormeGeometrique forme = new Carre(4);
		System.out.println("Le " + forme.getNom() + " a pour perimetre : " + forme.getPerimetre());
		forme = new Rectangle(4, 5);
		System.out.println("Le " + forme.getNom() + " a pour perimetre : " + forme.getPerimetre());
		forme = new Triangle(4, 5, 6);
		System.out.println("Le " + forme.getNom() + " a pour perimetre : " + forme.getPerimetre());
		forme = new Quadri(4, 5, 6, 7);
		System.out.println("Le " + forme.getNom() + " a pour perimetre : " + forme.getPerimetre());
		forme = new Cercle(5);
		System.out.println("Le " + forme.getNom() + " a pour perimetre : " + forme.getPerimetre());
	}

}

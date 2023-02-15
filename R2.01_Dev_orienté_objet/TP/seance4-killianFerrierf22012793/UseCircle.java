public class UseCircle {
	public static void main(String[] args) {
		Circle c1 = new Circle();
		Circle c2 = new Circle(2,2,5);
		System.out.printf("Cercle 1 : Centre X = %d, Centre Y = %d, Rayon = %.2f\n",c1.getCenterX(), c1.getCenterY(), c1.getRadius());
		System.out.printf("Cercle 2 : Centre X = %d, Centre Y = %d, Rayon = %.2f\n",c2.getCenterX(), c2.getCenterY(), c2.getRadius());
		c2.setCenter(3,3);
		System.out.printf("Cercle 2 centre modifié : Centre X = %d, Centre Y = %d, Rayon = %.2f\n",c2.getCenterX(), c2.getCenterY(), c2.getRadius());
		c2.setRadius(40);
		System.out.printf("Cercle 2 rayon modifié : Centre X = %d, Centre Y = %d, Rayon = %.2f\n",c2.getCenterX(), c2.getCenterY(), c2.getRadius());
		c2.moveX(5);
		System.out.printf("Cercle 2 déplacé X : Centre X = %d, Centre Y = %d, Rayon = %.2f\n",c2.getCenterX(), c2.getCenterY(), c2.getRadius());
		c2.moveY(5);
		System.out.printf("Cercle 2 déplacé Y : Centre X = %d, Centre Y = %d, Rayon = %.2f\n",c2.getCenterX(), c2.getCenterY(), c2.getRadius());
		c2.translate(5);
		System.out.printf("Cercle 2 déplacé : Centre X = %d, Centre Y = %d, Rayon = %.2f\n",c2.getCenterX(), c2.getCenterY(), c2.getRadius());
	}
}
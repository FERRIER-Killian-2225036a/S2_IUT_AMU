public class UsePoint {
	public static void main(String[] args) {
		Point p1 = new Point(3,3);
		System.out.printf("Coordonnées du point 1 : X = %d, Y = %d\n",p1.getX(), p1.getY());
		Point p2 = new Point(5,2);
		System.out.printf("Coordonnées du point 2 : X = %d, Y = %d\n",p2.getX(), p2.getY());
		p2.translate(2);
		System.out.printf("Les coordonnées du point 2 après une translation de 3 : X = %d, Y = %d\n",p2.getX(), p2.getY());
		System.out.printf("La distance entre les deux est de %f\n", p1.distance(p2));

	}
}
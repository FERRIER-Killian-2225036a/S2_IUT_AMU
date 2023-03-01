package exo2;

public class Cercle extends FormeGeometrique {
	protected int rayon;
	
	public Cercle(int rayon) {
		super("Cercle");
		this.rayon = rayon;
	}
	public Cercle() {
		this(1);
	}
	
	@Override
	public double getPerimetre() {
		return 2 * Math.PI * rayon;
	}
}

package exo1;

public class PointColore extends Point {
	
	private int couleur;
	
	public PointColore(int ab, int or, int couleur) {
		super(ab, or);
		this.couleur = couleur;
	}
	
	public PointColore(int n) {
		super(n);
		this.couleur = 1;
	}
	
	public PointColore() {
		this.couleur = 1;
	}

	@Override
	public String toString() {
		return "PointColore(" + ab + ", " + or + ", " + couleur + ")";
		// return super.toString() + "de couleur : " + couleur;
	}
	
	public PointColore getSymetrie() {
		return new PointColore(-ab, -or, -couleur);
	}
}

package exo2;

public abstract class FormeGeometrique {
	protected String nom;
	
	public FormeGeometrique(String nom) {
		this.nom = nom;
	}
	public FormeGeometrique() {
		nom = null;
	}
	
	abstract public double getPerimetre();
	
	public String getNom() {
		return nom;
	}

}

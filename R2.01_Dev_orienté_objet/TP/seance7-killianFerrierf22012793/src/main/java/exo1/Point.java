package exo1;

public class Point {
	protected int ab, or;
	
	public Point(int ab, int or) {
		this.ab = ab;
		this.or = or;
	}
	public Point(int n) {
		this(n, n);
	}
	public Point() {
		this(0, 0);
	}
	
	public int getAb() {
		return ab;
	}
	public int getOr() {
		return or;
	}
	
	public void setAb(int ab) {
		this.ab = ab;
	}
	public void setOr(int or) {
		this.or = or;
	}
	
	public void translate(int n) {
		ab += n;
		or += n;
	}
	public Point getSymetrie() {
		return new Point(-ab, -or);
	}
	
	@Override
	public String toString() {
		return "Point(" + ab + ", " + or + ")";
	}
	
}

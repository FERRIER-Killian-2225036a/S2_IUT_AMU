public class Point {
	private int x,y;
	public Point() {
		this.x = 0;
		this.y = 0;
	}
	public Point(int n) {
		this.x = n;
		this.y = n;
	}
	public Point(int x, int y) {
		this.x = x;
		this.y = y;
	}
	public int getX() {
		return x;
	}
	public int getY() {
		return y;
	}
	public void setX(int x) {
		this.x = x;
	}
	public void setY(int y) {
		this.y = y;
	}
	public void translate(int n) {
		this.x += n;
		this.y += n; 
	}
	public double distance(Point p2) {
		return Math.sqrt(Math.pow(p2.getX() - this.getX(), 2) + Math.pow(p2.getY() - this.getY(), 2));
	}
}
public class Circle {
	private Point center = new Point();
	private double radius;
	public Circle() {
		center.setX(0);
		center.setY(0);
		radius = 10;
	}
	public Circle(int x, int y, double radius) {
		this.center.setX(x);
		this.center.setY(y);
		this.radius = radius;
	}
	public int getCenterX() {
		return center.getX();
	}
	public int getCenterY() {
		return center.getY();
	}
	public double getRadius() {
		return radius;
	}
	public void setCenter(int x, int y) {
		center.setX(x);
		center.setY(y);
	}
	public void setRadius(double radius) {
		this.radius = radius;
	}
	public void translate(int n) {
		center.translate(n);
	}
	public void moveX(int x) {
		center.setX(center.getX()+x);
	}
	public void moveY(int y) {
		center.setY(center.getY()+y);
	}
}
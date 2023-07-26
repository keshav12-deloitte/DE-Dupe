import java.lang.Math;

public class HelperMethods {
    private int constantVariable;
    public int publicVar;

    /**
     * This method adds two numbers and returns the square root of their sum
     * added with the value of publicVar.
     *
     * @param num1 the first number
     * @param num2 the second number
     * @return the result of the addition
     */
    public double add(int num1, int num2) {
        System.out.println(this.constantVariable);
        return Math.sqrt(num1 + num2) + this.publicVar;
    }

    /**
     * Multiplies two numbers and returns the result.
     *
     * @param num1 the first number
     * @param num2 the second number
     * @return the result of the multiplication
     */
    public double multiply(double num1, double num2) {
        return Math.sin(num1 * num2) * this.oddVar * this.oldMethod();
    }

    /**
     * Returns the value of oddVar.
     *
     * @return The value of oddVar.
     */
    private int oddMethod() {
        return this.oddVar;
    }

    /**
     * This is the function to print name
     *
     * @param constant String
     * @return constant
     */
    public static String just_print(String constant) {
        return constant;
    }
}

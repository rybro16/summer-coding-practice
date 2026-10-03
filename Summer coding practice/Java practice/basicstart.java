import java.util.Scanner;
// The class name must match the file name: basicstart.java.
public class basicstart{
    // Java starts running the program from here.
    // public means Java is allowed to access it.
    // static means Java can run it without creating an object first.
    // void means this method does not return a value.
    // String[] args is a place for text values passed in when the program starts.    
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("What is your name? ");
        String name = input.nextLine();
        System.out.println("Hello," + name + "!");
        // Print "Hello!" on the screen, then move to a new line.
        System.out.println("Hello!");
        // Print "I'm learning Java" on the screen, then move to a new line.
        System.out.println("I'm learning Java");

        // Variables
        int age = 18;

        System.out.println(name);
        System.out.println(age);

    }
}


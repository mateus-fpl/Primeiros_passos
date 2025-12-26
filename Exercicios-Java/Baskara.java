import java.util.Scanner;

public class Baskara {

    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        double a, b, c, delta, x1, x2;
        System.out.print("Digite a: ");
        a = scanner.nextDouble();
        System.out.print("Digite b: ");
        b = scanner.nextDouble();
        System.out.print("Digite c: ");
        c = scanner.nextDouble();

        if ( a == 0){
            System.out.println("Nao é de segundo grau");
        }
        else {
            delta = b*b - 4*a*c;
                if (delta < 0){
                    System.out.println("Nao tem raiz real");
                } else if(delta >0) {
                    x1 = (-b - Math.sqrt(delta))/(2*a);
                    x2 = (-b + Math.sqrt(delta))/(2*a);
                    System.out.println("x1 = " + x1);
                    System.out.println("x2 = " + x2);
                } else {//delta é zero
                    x1 = -b / (2*a);
                    System.out.println("raiz unica: " + x1);
                }
        }

        scanner.close();
    }
  
}
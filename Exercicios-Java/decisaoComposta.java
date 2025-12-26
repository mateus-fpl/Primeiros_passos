import java.util.Scanner;
public class decisaoComposta {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite os lados de um triângulo:");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();

        if (a+b > c && a+c > b && b+c > a) {
            if (a == b && b==c){
                System.out.print("Triangulo Equilátero");
            } else if(a==b || a==c || b==c){
                System.out.print("Triangulo Isóceles");
            } else {
                System.out.print("Triangulo Escaleno");
            };
        } else {
            System.out.println("Não é um triângulo!");
        }

        scanner.close();
    }
}

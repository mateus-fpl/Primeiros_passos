import java.util.Scanner;
public class Combustivel {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite a distancia percorrida em KM:");
        int km = scanner.nextInt();
        System.out.println("Digite a quantidade de litros consumida:");
        int litros = scanner.nextInt();
        double consumo = km/litros;
        if (consumo < 8){
            System.out.println("Venda o carro!");
        } else if( consumo < 12) {
            System.out.println("Econômico!");
        } else {
            System.out.println("Super econômico!");
        }

        scanner.close();
    }
}

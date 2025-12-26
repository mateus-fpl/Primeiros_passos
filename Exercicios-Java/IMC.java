import java.util.Scanner;

public class IMC {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu peso:");
        double peso = scanner.nextDouble();
        System.out.println("Digite sua altura:");
        double altura = scanner.nextDouble();
        double IMC = peso/(altura*altura);

        if (IMC < 18.5){
            System.out.println("Abaixo do peso");
        }
        else if (IMC < 24.9){
            System.out.println("Peso ideal");
        }
        else if (IMC < 29.9){
            System.out.println("Levemente acima do peso");
        }
        else if (IMC < 34.9){
            System.out.println("Obesidade Grau I");
        } 
        else if (IMC < 39.9){
            System.out.println("Obesidade Grau II (Severa)");
        }
        else {
            System.out.println("Obesidade Grau III (Mórbida)");
        }
    
    
    
    }
    
}

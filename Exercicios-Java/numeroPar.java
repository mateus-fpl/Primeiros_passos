import java.util.Scanner;

public class numeroPar {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero;
        do {
            System.out.println("Digite um número par: ");
            numero = scanner.nextInt();
        } while (numero%2 == 1);
        int contador = 0;
        do{
            System.out.print(contador + " ");
            contador = contador + 2;
           
        } while (contador <= numero);
            scanner.close();            
        }
    }


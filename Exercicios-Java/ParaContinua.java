//rodar o programa até que o usuário digite p/P para parar

import java.util.Scanner;

public class ParaContinua {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);  
        System.out.println("Digite p para parar ou outro para continuar: ");
        char opcao = scanner.nextLine().charAt(0);
        while (opcao != 'p' && opcao != 'P'){
            System.out.println("Digite p para parar ou outro para continuar: ");
            opcao = scanner.nextLine().charAt(0);
        }  
        System.out.println("Obrigado, volte sempre");
        scanner.close();
    }
}

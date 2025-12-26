import java.util.Scanner;

public class repet8 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int i=0;
        System.out.println("Digite o primeiro número:");
        int entrada = scanner.nextInt();
        int maiorValor = entrada;
        int menorValor = entrada;
        System.out.println("Digite dez valores:");
        for (i=0; i<10;i++){
            entrada = scanner.nextInt();
            
            if (entrada > maiorValor){
                 maiorValor = entrada;
            }
            if (entrada < menorValor){
            menorValor = entrada;
            }
        }
        System.out.println("O maior valor é: " + maiorValor);
        System.out.println("O maior valor é: " + menorValor);

        scanner.close();
    }
}

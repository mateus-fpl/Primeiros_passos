//Desenvolver um programa que lê certa quantidade de números e imprime o maior deles e a quantidade
//de vezes que esse foi lido.

import java.util.Scanner;

public class MaiorDaLista {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //ler um inteiro positivo, com validação
        int n;
        do { 
            System.out.print("Digite um inteiro positivo: ");
            n = scanner.nextInt();
        } while (n <= 0);
        //CERTEEEEEEEEEZA QUE N É POSITIIIIIIVO
        System.out.println("Digite o primeiro valor:");
        int valor = scanner.nextInt();
        int maior = valor;
        int vezes = 1;
        for (int i = 1; i < n; i++){
            valor = scanner.nextInt();
            if (valor > maior) {
                maior = valor;
                vezes = 1;
            } else if (valor == maior) {
                vezes++;
            }
        }
        System.out.println("o maior valor e " + maior + " ele apareceu " + vezes + " vezes");
        scanner.close();
    }
}

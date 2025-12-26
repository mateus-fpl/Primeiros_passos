 //ler uma sequência de números até que o usuário digite -1, contar quantos números foram digitados
//e exibir no final

import java.util.Scanner;

public class SomaNumeros {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int numero,contador = 0;
        //no código a seguir, contamos um a mais
        do { 
            System.out.println("Digite sua sequencia, -1 encerra: ");
            numero = scanner.nextInt();
            contador = contador + 1;
        } while (numero != -1);
        //primeira saída: exibir o contador -1
        System.out.println("Foram digitados " + (contador -1) + " valores");
        //na solução a seguir, vamos testar dentro do laço
        //custo alto: dois testes para a mesma situação
        contador = 0;
        do { 
            System.out.println("Digite sua sequencia, -1 encerra: ");
            numero = scanner.nextInt();
            if (numero != -1){
            contador = contador + 1;
            }
        } while (numero != -1);
        System.out.println("Foram digitados " + contador + " valores");

        //o código a seguir o teste no início, eliminando o teste interno
        contador = 0;
        System.out.println("Digite sua sequencia, -1 encerra: ");
        numero = scanner.nextInt();
        while (numero != -1){
            contador++;
            System.out.println("Digite sua sequencia, -1 escreva:");
            numero = scanner.nextInt();
        }
        System.out.println("Foram digitados " + contador + " valores");
    }
}

//Ler um inteiro positivo e mostrar todos os seus dígitos

import java.util.Scanner;

public class DescascaNumero {
    public static void main(String[] args) {
     Scanner scanner = new Scanner(System.in);
     System.out.print("Digite um numero inteiro:");  
     int n = scanner.nextInt();
     while (n >0) {
        System.out.println(n%10); 
        n = n/10;
    }
    scanner.close();
    }
}

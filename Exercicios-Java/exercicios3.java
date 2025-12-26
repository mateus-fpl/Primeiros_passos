import java.util.Scanner;

public class exercicios3 {
    public static void main (String[] args){
        var scanner = new Scanner(System.in);
        System.out.println("Coloque a base do retângulo:");
        var  base = scanner.nextDouble();
        System.out.println("Coloque a altura do retângulo:");
        var high = scanner.nextDouble();
        var area = base*high;
        System.out.println("A área do retângulo é: \n" + area);
    }
    
}

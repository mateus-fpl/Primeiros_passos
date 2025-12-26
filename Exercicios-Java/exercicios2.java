import java.util.Scanner;
public class exercicios2 {
    public static void main (String[] args){
        var scanner = new Scanner(System.in);
        System.out.println("Informe um lado do quadrado:");
        var side = scanner.nextDouble();
        var area = side*side;
        System.out.printf("A área do quadrado é: \n" + area);

    }
    
}

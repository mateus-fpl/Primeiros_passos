import java.util.Scanner;

public class multiplicacao {
    public static void main(String[] args){
        System.out.println("Por favor, digite um número:");
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();

        for (int i=0; i<11; i++){
            int result = number * i;
            System.out.println(number + " x " + i + " = " + result);
        }
        scanner.close();
    }
    
}

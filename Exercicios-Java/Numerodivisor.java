import java.util.Scanner;

public class Numerodivisor {
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Informe um número:");
        int number = scanner.nextInt();
        boolean keepVerify = true;

        while (keepVerify){
            System.out.println("Informe um número para verificação:");
            int toVerify = scanner.nextInt();
            if (toVerify <0){
                System.out.printf("Informe um número maior que %s \n", number);
                continue;
            }
           
            keepVerify = toVerify % number == 0;
            System.out.printf("%s %% %s = %s ", toVerify, number, keepVerify);
            
            }
    }
    
}

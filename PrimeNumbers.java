import java.util.Scanner;
public class PrimeNumbers
{
    public static void main(String[] args)
    {
        int i;
        java.util.Scanner scanner = new java.util.Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = scanner.nextInt();
        System.out.printf("The prime factors of %d are: ", n);

        if (n % 2 == 0)
        {
            System.out.print("2 ");
            while (n % 2 == 0)
            {
                n = n / 2;
            }
        }
        for (i = 3; i * i <= n; i += 2)
        {
            if (n % i == 0)
                System.out.printf("%d ", i);
            while (n % i == 0)
            {
                n = n / i;
            }
        }

        if (n > 2)
        {
            System.out.printf("%d ", n);
        }
        scanner.close();
    }
}
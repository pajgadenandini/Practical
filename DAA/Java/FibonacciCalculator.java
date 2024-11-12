import java.util.Scanner;

public class FibonacciCalculator {

    // Recursive Fibonacci function with step count
    public static int fibonacciRecursive(int n, int[] steps) {
        steps[0]++; // Each call is counted as a step
        if (n <= 1) {
            return n;
        }
        return fibonacciRecursive(n - 1, steps) + fibonacciRecursive(n - 2, steps);
    }

    // Iterative Fibonacci function with step count
    public static int[] fibonacciIterative(int n) {
        if (n <= 1) {
            return new int[] { n, 1 }; // Base case with 1 step
        }

        int prev = 0, curr = 1;
        int steps = 2; // Initial step for the base values

        for (int i = 2; i <= n; i++) {
            int temp = curr;
            curr = prev + curr;
            prev = temp;
            steps++; // Increment step for each iteration
        }

        return new int[] { curr, steps };
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the position of Fibonacci number: ");
        int n = scanner.nextInt();

        // Recursive calculation
        int[] stepsRecursive = { 0 }; // Array to hold step count by reference
        int fibRecursive = fibonacciRecursive(n, stepsRecursive);
        System.out.println("Recursive: The " + n + "th Fibonacci number is: " + fibRecursive);
        System.out.println("Total steps taken (recursive): " + stepsRecursive[0]);

        // Iterative calculation
        int[] fibIterative = fibonacciIterative(n);
        System.out.println("Iterative: The " + n + "th Fibonacci number is: " + fibIterative[0]);
        System.out.println("Total steps taken (iterative): " + fibIterative[1]);
    }
}

// Complexity Analysis
// Recursive Approach:

// Time Complexity:
// 𝑂(2^𝑛), due to redundant calculations.
// Space Complexity:
// 𝑂(𝑛), due to recursion stack depth.
// Iterative Approach:

// Time Complexity:
// 𝑂(𝑛), as each number up to n is calculated once.
// Space Complexity:
// 𝑂(1)
// if we only track the last two values in the sequence.

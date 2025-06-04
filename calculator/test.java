

class test {
    public static void main(String[] args) {
        int i = 1;

        int a = ++i;
        int b = i++;

        System.out.println("a: " + a); // Output: a: 1
        System.out.println("b: " + b); // Output: b: 3
    }
}
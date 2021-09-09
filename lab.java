public class lab {
    public static void main(String args[]) {
        double b[][] = new double[6][20];
        float x[] = new float[20];
        short a[] = new short[6];
        for (int i = 0; i < x.length; i++) {
            double num = Math.random() * 25;
            num = num - 14.0f;
            float num1 = (float) num;
            x[i] = num1;
        }
        int k = 0;
        for (short i = 6; i <= 16; i++) {
            if (i % 2 == 0) {
                a[k] = i;
                k++;
            }
        }
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 20; j++) {
                if (a[i] == 14) {
                    double number = Math.abs(x[j]);
                    double num1 = 1.0 / 3.0;
                    number = Math.pow(number, num1);
                    number = -number;
                    b[i][j] = Math.asin(Math.pow(Math.E, number));
                }
                if (a[i] == 6 | a[i] == 8 | a[i] == 12) {
                    double p1 = Math.cos(x[j]);
                    p1 = Math.pow(p1, 2);
                    p1 = Math.abs(p1);
                    p1 = Math.pow(p1, 1.0 / 3.0);
                    p1 = -p1;
                    b[i][j] = Math.atan(Math.pow(Math.E, p1));
                } else {
                    double p2 = Math.cos(x[i]);
                    double p3 = Math.sin(x[i]);
                    p2 = Math.abs(p2);
                    double p4 = Math.pow(Math.E, p2);
                    p2 = -p2;
                    p3 = Math.abs(p3);
                    double p5 = Math.pow(p3, 2 * p4);
                    p5 = Math.abs(p5);
                    p5 = Math.pow(p5, 1.0 / 3.0);
                    p5 = -p5;
                    b[i][j] = Math.atan(Math.pow(Math.E, p5));
                }
            }
        }
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 20; j++) {
                String answer = String.format("%.3f", b[i][j]);
                System.out.print(" " + answer + " ");
            }
            System.out.println();
        }
    }
}

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class solution {
    public static void main(String[] args) throws FileNotFoundException {
        int ans1 = 0;
        int ans2 = 0;
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        try {
            while (reader.ready()) {
                String [] line = reader.readLine().split(",|-");
                if (Integer.parseInt(line[0]) <= Integer.parseInt(line[2]) && Integer.parseInt(line[1]) >= Integer.parseInt(line[3])){
                    ans1 += 1;
                    ans2 += 1;
                }
                else if (Integer.parseInt(line[0]) >= Integer.parseInt(line[2]) && Integer.parseInt(line[1]) <= Integer.parseInt(line[3])){
                    ans1 += 1;
                    ans2 += 1;
                }
                else if (Integer.parseInt(line[0]) <= Integer.parseInt(line[2]) && Integer.parseInt(line[2]) <= Integer.parseInt(line[1])){
                    ans2 += 1;
                }
                else if (Integer.parseInt(line[2]) <= Integer.parseInt(line[0]) && Integer.parseInt(line[0]) <= Integer.parseInt(line[3])){
                    ans2 += 1;
                }
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        System.out.println(ans1);
        System.out.println(ans2);
    }
}

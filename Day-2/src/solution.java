import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

public class solution{
    public static void main(String[] args) throws FileNotFoundException {
        int score = 0;
        int score2 = 0;
        BufferedReader reader = new BufferedReader(new FileReader("input.txt"));
        try{
            String line;
            while (reader.ready()) {
                line = reader.readLine();
                String[] moves = line.split(" ");
                if (moves[1].equals("X")){
                    score += 1;
                    if (moves[0].equals("A")){
                        score += 3;
                        score2 += 3;
                    }
                    if (moves[0].equals("B")){
                        score2 += 1;
                    }
                    if (moves[0].equals("C")){
                        score += 6;
                        score2 += 2;
                    }
                }
                if (moves[1].equals("Y")){
                    score += 2;
                    score2 += 3;
                    if (moves[0].equals("A")){
                        score += 6;
                        score2 += 1;
                    }
                    if (moves[0].equals("B")){
                        score += 3;
                        score2 += 2;
                    }
                    if (moves[0].equals("C")){
                        score2 += 3;
                    }
                }
                if (moves[1].equals("Z")){
                    score += 3;
                    score2 += 6;
                    if (moves[0].equals("A")){
                        score2 += 2;
                    }
                    if (moves[0].equals("B")){
                        score += 6;
                        score2 += 3;
                    }
                    if (moves[0].equals("C")){
                        score += 3;
                        score2 += 1;
                    }
                }
        }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        System.out.println(score);
        System.out.println(score2);
    }
}

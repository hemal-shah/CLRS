
import java.io.*;
import java.util.ArrayList;

/**
 * Created by hemal on 25/5/17.
 */
public class HeapSort {


    static int RIGHT(int index) {
        return (index * 2) + 2;
    }

    static int LEFT(int index) {
        return (index * 2) + 1;
    }

    private static ArrayList<Integer> MAX_HEAPIFY(ArrayList<Integer> A, int index, int length) {

        int left_index = LEFT(index);
        int right_index = RIGHT(index);
        int largest_index;

        if (left_index <= length && A.get(left_index) > A.get(index)) {
            largest_index = left_index;
        } else {
            largest_index = index;
        }
        if (right_index <= length && A.get(right_index) > A.get(largest_index)) {
            largest_index = right_index;
        }

        if(largest_index != index){
            //Swaping values at index and largest_index
            A = swapValues(A, largest_index, index);

            //Now calling max heapify on largest index, as it should be a child of original value index.
            A = MAX_HEAPIFY(A, largest_index, length);
        }

        return A;
    }

    static ArrayList<Integer> swapValues(ArrayList<Integer> A, int index1, int index2){
        int temp = A.get(index1);
        A.set(index1, A.get(index2));
        A.set(index2, temp);
        return A;
    }

    private static ArrayList<Integer> BUILD_MAX_HEAP(ArrayList<Integer> A){
        for(int i = A.size()/2; i >= 0; i--){
            A = MAX_HEAPIFY(A, i, A.size() - 1);
        }
        return A;
    }



    static ArrayList<Integer> readData(String location){

        ArrayList<Integer> A = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(location))) {
            String data;
            while ((data = br.readLine()) != null) {
                A.add(Integer.parseInt(data));
            }
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }

        return A;
    }

    public static void main(String[] args) {

        String location = "/home/hemal/Programs/Testing/HeapSort/src/input.txt";
        ArrayList<Integer> A = readData(location);
        A = BUILD_MAX_HEAP(A);

        for(int i = A.size() - 1; i >= 1; i--){
            // Swap the values at i and 0
            A = swapValues(A, 0, i);

            //Now call max_heapify again over and over, with 1 length less.
            A = MAX_HEAPIFY(A, 0, i - 1);
        }

        System.out.println(A);
    }
}
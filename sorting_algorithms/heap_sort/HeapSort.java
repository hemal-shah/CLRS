import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

/**
 * Created by hemal on 25/5/17.
 */
public class HeapSort {

    /**
     * Generally should return i*2 for the heap, but as we have index
     * starting at 0, we are returning (i*2) + 1 to adjust the bit.
     *
     * Applicable for binary heaps only.
     * @param i
     * @return
     */
    private static int LEFT(int i){
        return (i*2) + 1;
    }

    /**
     * Same as above, but returns (i*2) + 2 to adjust for the discrepancy.
     * @param i
     * @return
     */
    private static int RIGHT(int i){
        return (i*2) + 2;
    }


    /**
     * Max-heapifies any given input list, from the point of index provided.
     * MAX-HEAPIFY maintains following property for a heap:
     *
     * A[parent] >= A[i] for i being a root/index.
     *
     * @param list
     * @param index
     * @return
     */
    private static ArrayList<Integer> MAX_HEAPIFY(ArrayList<Integer> list,
                                                  int index,
                                                  int length){

        int largest;
        int left = LEFT(index);
        int right = RIGHT(index);

        if(left <= length && list.get(left) > list.get(index))
            largest = left;
        else
            largest = index;

        if(right <= length && list.get(right) > list.get(largest))
            largest = right;


        if(largest != index){
            int temp = list.get(largest);
            list.set(largest, list.get(index));
            list.set(index, temp);
            list = MAX_HEAPIFY(list, largest, length);
        }

        //return the modified list.
        return list;
    }

    private static ArrayList<Integer> BUILD_MAX_HEAP(ArrayList<Integer> list){
        int halfway = list.size()/2;

        for(int i = halfway; i >= 0; i--){
            list = MAX_HEAPIFY(list, i, list.size() - 1);
        }
        return list;
    }

    public static void main(String[] args) {

        ArrayList<Integer> list = new ArrayList<>();

        //Enter your own location of "\n" separated numbers as a text file.
        static String location = "/home/hemal/Programs/Testing/HeapSort/src/input.txt";
        try(BufferedReader br = new BufferedReader(new FileReader(location))){
            String in;
            int i = 0;
            while((in = br.readLine()) != null){
                list.add(Integer.parseInt(in));
            }
        }catch (IOException exception){
            System.out.println(exception.toString());
        }

        list = BUILD_MAX_HEAP(list);
        for (int i = list.size() - 1; i >= 1; i--){
            int temp = list.get(0);
            list.set(0, list.get(i));
            list.set(i, temp);
            list = MAX_HEAPIFY(list, 0, i - 1);
        }

        System.out.println(list);
    }
}

import java.util.ArrayList;

/**
 * Created by hemal on 25/5/17.
 */
public class ReverseHeapSort {

    private static ArrayList<Integer> MIN_HEAPIFY(ArrayList<Integer> A, int index, int length) {
        int left_index = HeapSort.LEFT(index);
        int right_index = HeapSort.RIGHT(index);
        int smallest_value_index;

        if (left_index <= length && A.get(left_index) < A.get(index)) {
            smallest_value_index = left_index;
        } else {
            smallest_value_index = index;
        }

        if (right_index <= length && A.get(right_index) < A.get(smallest_value_index)) {
            smallest_value_index = right_index;
        }

        if (smallest_value_index != index) {
            //Swap values at smallest_value_index and index
            A = HeapSort.swapValues(A, smallest_value_index, index);
            A = MIN_HEAPIFY(A, smallest_value_index, length);
        }
        return A;
    }

    private static ArrayList<Integer> BUILD_MIN_HEAP(ArrayList<Integer> A) {
        for (int i = A.size() / 2; i >= 0; i--) {
            A = MIN_HEAPIFY(A, i, A.size() - 1);
        }
        return A;
    }

    public static void main(String[] args) {
        String location = "/home/hemal/Programs/Testing/HeapSort/src/input.txt";
        ArrayList<Integer> A = HeapSort.readData(location);

        A = BUILD_MIN_HEAP(A);

        for (int i = A.size() - 1; i >= 1; i--) {
            //Swap values at 0 and i
            A = HeapSort.swapValues(A, 0, i);
            //calling min_heapify here again
            A = MIN_HEAPIFY(A, 0, i - 1);
        }

        System.out.println(A);
    }
}

package quick_sort;

import heap_sort.HeapSort;

import java.util.ArrayList;

/**
 * Code is developed by
 * hemal on 28/5/17 at 1:26 AM.
 * <p>
 * Contact hemal at email : hemal.shah1996@gmail.com
 */

public class QuickSort {

    /**
     * Class created so that I can return two values from
     * a function call.
     * <p>
     * I need to create two returning values from method call,
     * because in recursive call, I have to have updated ArrayList
     * and then apply that ArrayList for further calls.
     * <p>
     * So, even though Java is pass-by-value language,
     * the updated ArrayList would be discarded after successful completion
     * of one recursive call, which should not happen, as we need this updated ArrayList.
     */
    class Holder {
        int q;
        ArrayList<Integer> A;

        int getQ() {
            return q;
        }

        void setQ(int q) {
            this.q = q;
        }

        ArrayList<Integer> getA() {
            return A;
        }

        void setA(ArrayList<Integer> a) {
            A = a;
        }
    }

    private ArrayList<Integer> QUICK_SORT(ArrayList<Integer> A, int start, int end) {
        if (start < end) {
            Holder holder = new Holder();
            holder.setA(A);
            holder = PARTITION(holder, start, end);
            int q = holder.getQ();
            A = QUICK_SORT(A, start, q - 1);
            A = QUICK_SORT(A, q + 1, end);
        }
        return A;
    }

    private static Holder PARTITION(Holder holder, int start, int end) {
        //set q here
        int i = start - 1;
        ArrayList<Integer> A = holder.getA();
        int x = A.get(end);
        for (int j = start; j < end; j++) {
            if (A.get(j) <= x) {
                i++;
                if (i != j) {
                    /*
                     * An additional check to save some swap time when both index point at same
                     * location.
                     * For few swaps it doesn't matter,
                     * but when we have huge data set to sort, it matters.
                     */
                    A = HeapSort.swapValues(A, i, j);
                }
            }
        }

        A = HeapSort.swapValues(A, i + 1, end);
//        System.out.println(A);
        holder.setA(A);
        holder.setQ(i + 1);
        return holder;
    }


    public static void main(String[] args) {
        String location = "/home/hemal/Programs/Testing/HeapSort/src/input.txt";
        ArrayList<Integer> A = HeapSort.readData(location);
        QuickSort sort = new QuickSort();
        A = sort.QUICK_SORT(A, 0, A.size() - 1);
        System.out.println(A);
    }
}

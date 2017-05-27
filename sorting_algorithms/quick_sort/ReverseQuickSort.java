package quick_sort;

import heap_sort.HeapSort;

import java.util.ArrayList;

/**
 * Code is developed by
 * hemal on 28/5/17 at 1:36 AM.
 * <p>
 * Contact hemal at email : hemal.shah1996@gmail.com
 */
public class ReverseQuickSort {

    class Holder{
        int fix_positioned_number_index;
        ArrayList<Integer> A;

        int getFix_positioned_number_index() {
            return fix_positioned_number_index;
        }

        void setFix_positioned_number_index(int fix_positioned_number_index) {
            this.fix_positioned_number_index = fix_positioned_number_index;
        }

        ArrayList<Integer> getA() {
            return A;
        }

        void setA(ArrayList<Integer> a) {
            A = a;
        }
    }

    private ArrayList<Integer> REVERSE_QUICK_SORT(ArrayList<Integer> A, int start, int end) {
        if (start < end) {
            Holder  holder = new Holder();
            holder.setA(A);
            holder = PARTITION(holder, start, end);
            int q = holder.getFix_positioned_number_index();
            A = REVERSE_QUICK_SORT(A, start, q - 1);
            A = REVERSE_QUICK_SORT(A, q + 1, end);
        }
        return A;
    }

    private static Holder PARTITION(Holder holder, int start, int end){

        ArrayList<Integer> A = holder.getA();
        int x = A.get(end);
        int i = start - 1;

        for(int j = start; j < end; j++){
            if (A.get(j) >= x){
                i++;
                if( i != j){
                    A = HeapSort.swapValues(A, i, j);
                }
            }
        }

        A = HeapSort.swapValues(A, i + 1, end);
        holder.setA(A);
        holder.setFix_positioned_number_index(i + 1);
        return holder;
    }

    public static void main(String[] args) {
        String location = "/home/hemal/Programs/Testing/HeapSort/src/input.txt";
        ArrayList<Integer> A = HeapSort.readData(location);

        ReverseQuickSort sort = new ReverseQuickSort();

        A = sort.REVERSE_QUICK_SORT(A, 0, A.size() - 1);
        System.out.println(A);
    }
}

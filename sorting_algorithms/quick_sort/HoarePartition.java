package quick_sort;

import heap_sort.HeapSort;

import java.util.ArrayList;

/**
 * Code is developed by
 * hemal on 28/5/17 at 2:29 AM.
 * <p>
 * Contact hemal at email : hemal.shah1996@gmail.com
 */
public class HoarePartition {

    private class Holder {
        int q;
        ArrayList<Integer> list;

        Holder(ArrayList<Integer> list) {
            this.list = list;
        }

        int getQ() {
            return q;
        }

        void setQ(int q) {
            this.q = q;
        }

        ArrayList<Integer> getList() {
            return list;
        }

        void setList(ArrayList<Integer> list) {
            this.list = list;
        }
    }

    private ArrayList<Integer> QUICK_SORT(ArrayList<Integer> list, int start, int end) {
        if (start < end) {
            Holder holder = new Holder(list);
            Holder holder1 = HOARE_PARTITION(holder, start, end);
            int q = holder1.getQ();
            list = holder1.getList();
            list = QUICK_SORT(list, start, q - 1);
            list = QUICK_SORT(list, q + 1, end);
        }
        return list;
    }

    private static Holder HOARE_PARTITION(Holder holder, int start, int end) {
        ArrayList<Integer> list = holder.getList();
        int x = list.get(start);
        int i = start;
        int j = end;

        while (true) {
            while (j >= start && list.get(j) > x) {
                j--;
            }
            while (i <= end && list.get(i) < x) {
                i++;
            }

            if (i < j) {
                list = HeapSort.swapValues(list, i, j);
            } else {
                //We still need to swap the values to index j
                list = HeapSort.swapValues(list, j, list.indexOf(x));
                holder.setList(list);
                holder.setQ(j);
                return holder;
            }
        }
    }

    public static void main(String[] args) {
        String location = "/home/hemal/Programs/Testing/HeapSort/src/input.txt";
        ArrayList<Integer> list = HeapSort.readData(location);
        System.out.println("Before Sorting :" + list);

        HoarePartition sort = new HoarePartition();
        list = sort.QUICK_SORT(list, 0, list.size() - 1);
        System.out.println(list);
    }

}

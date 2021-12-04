import java.lang.reflect.Array;
import java.util.Arrays;

/**
 * @Auther icebear
 * @Date 12/4/21
 */

public class QuickSort {
  public void quick_sort(int[] nums, int begin, int end){
//    快速排序实现办法
//    判断结束条件
    if (begin >= end){
      return;
    }
//    定义中间元素
    int middle = nums[begin];
//    定义左下标
    int left = begin;
//    定义右下标
    int right = end;
//    判断左下标是否小于右下标
    while (left < right) {
//      当左下标小于右下标且中间元素小于等于右边元素
      while(left < right & middle < nums[right]) {
//        将右下标左移
        right -= 1;
      }
//      将左右下标的值交换
      nums[left] = nums[right];
//      当左下标小于右下标且左下标元素小于中间元素
      while (left < right & middle >= nums[left]) {
//        将左下标右移
        left += 1;
      }
//      将左右下标的值交换
      nums[right] = nums[left];
//      将中间元素赋值给左下标元素
      nums[left] = middle;
//    分别递归遍历左右两边的元素
      quick_sort(nums, begin, left - 1);
      quick_sort(nums, left + 1, end);
    }
  }
  public static void main(String[] args) {
    QuickSort qs = new QuickSort();
    int[] nums = {3, 57, 48, 27, 12, 14, 1, 2, 5};
    System.out.println(Arrays.toString(nums));
    qs.quick_sort(nums, 0, nums.length - 1);
    System.out.println(Arrays.toString(nums));

  }
}

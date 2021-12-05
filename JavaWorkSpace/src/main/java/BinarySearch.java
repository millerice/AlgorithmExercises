/**
 * @Auther icebear
 * @Date 12/5/21
 */

import java.util.Arrays;

/**
 * 二分查找
 */
public class BinarySearch {

  public boolean binary_search(int[] nums, int target){
    // 定义最左边元素下标
    int left = 0;
    // 定义最右边元素下标
    int right = nums.length-1;
    // 判断左下标是否小于右下标
    while (left <= right) {
      // 定义中间元素下标
      int middle = left + (right - left)/2;
//      System.out.println(middle);
      // 判断中间元素是否等于目标元素
      if (nums[middle] == target) {
        // 是，返回true
        return true;
      }
      // 判断中间元素是否大于目标元素
      if (nums[middle] > target) {
        // 是，让右下标等于中间元素下标
        right = middle + 1;
      }
      // 判断中间元素是否小于目标元素
      if (nums[middle] < target) {
        // 是，让左下标等于中间元素下标
        left = middle - 1;
      }
    }
    // 返回 false
    return false;
  }

  public static void main(String[] args) {
    BinarySearch bs = new BinarySearch();
    int[] nums = {1, 3, 4, 6, 7, 8, 9, 10};
    System.out.println(bs.binary_search(nums, 6));
  }
}

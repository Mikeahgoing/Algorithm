/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let numMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    let res = target - nums[i];
    if (numMap.has(res)) {
      return [numMap.get(res), i];
    }
    numMap.set(nums[i], i);
  }
  return [];
};

console.log(twoSum([2,7,11,15],9));
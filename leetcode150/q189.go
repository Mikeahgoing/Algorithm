package main

import "fmt"

func rotate(nums []int, k int) []int {
	if k == 0 {
		return nums
	}
	if k > len(nums) {
		k = k % len(nums)
	}
	nums = append(nums[len(nums)-k:], nums[:len(nums)-k]...)
	return nums
}
func main() {
	ints := rotate([]int{1, 2, 3, 4, 5, 6, 7}, 3)
	fmt.Println(ints)
	rotate([]int{-1, -100, 3, 99}, 2)
}

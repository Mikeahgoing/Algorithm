package main

func majorityElement(nums []int) int {
	m := make(map[int]int)
	num := len(nums) / 2
	for _, v := range nums {
		value, ok := m[v]
		if ok {
			m[v] = value + 1
		} else {
			m[v] = 1
		}
	}
	for k, v := range m {
		if v > num {
			return k
		}
	}
	return 0
}

func main() {
	majorityElement([]int{3, 2, 3})
	majorityElement([]int{2, 2, 1, 1, 1, 2, 2})
}

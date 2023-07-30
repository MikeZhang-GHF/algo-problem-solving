const mergeSort = (nums: number[]): number[] => {
  if (nums.length <= 1)
      return nums

  //  divide
  const mid = nums.length >> 1
  const left = mergeSort(nums.slice(0, mid))
  const right = mergeSort(nums.slice(mid))
  // conquer
  let i = 0, j = 0, cur = 0
  const n = left.length, m = right.length
  while (true) {
      if (i == n) {
          nums.splice(cur, m - j, ...right.slice(j))
          break
      }
      if (j == m) {
          nums.splice(cur, n - i, ...left.slice(i))
          break
      }
      if (left[i] <= right[j]) nums[cur++] = left[i++]
      else nums[cur++] = right[j++]
  }
  return nums
}

const nums = [5, 2, 3, 1]
console.log(mergeSort(nums))
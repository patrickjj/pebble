'''Returns a pair inside an array that sum to the given total\
    Works for sorted arrays, but not unsorted'''

def find_pair_with_sum(array, target_sum):

  left_pointer = 0
  right_pointer = len(array) - 1

  while left_pointer < right_pointer:
    sum = array[left_pointer] + array[right_pointer]

    if sum == target_sum:
      return [array[left_pointer], array[right_pointer]]
    elif sum < target_sum:
      left_pointer += 1
    else:
      right_pointer -= 1

  return None

arr = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [8, 7, 6, 5, 4, 3, 2, 1]

print(find_pair_with_sum(arr, 10))
print(find_pair_with_sum(arr2, 10)) #fails

def find_pair_with_sum(array, target_sum):
    complements = {}
    for number in array:
        complement = target_sum - number
        if complement in complements:
            return [complement, number]
        complements[number] = True
    return None

print(find_pair_with_sum(arr2, 10))



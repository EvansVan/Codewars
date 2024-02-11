def partition(array,low,high):
  #keep track of pivot
  pivot = array[high]
  i = low - 1   
  for j in range(low,high):
    if array[j] <= pivot:
      i+=1
      array[i],array[j] = array[j], array[i]
  #swap for the pivot using I which was keeping track 
  array[i + 1], array[high] = array[high], array[i+1]
  return i + 1

def quicksort(array,low,high):
  if low < high:
    pi = partition(array,low,high)
    #sort left side
    quicksort(array,low,pi-1)
    #sorrt right side
    quicksort(array,pi+1,high)

if __name__ == '__main__':
    array = [11,9,29,7,2,15,28]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quicksort(array, 0, len(array)-1)
    print(array)
    
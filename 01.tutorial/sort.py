import random
import time


def ascending_comparator(a, b):
    if a > b:
        return 1
    if a < b:
        return -1
    return 0


def descending_comparator(a, b):
    return -ascending_comparator(a, b)


def bubble_sort(input_array, comparator):
    copy_array = input_array[:]
    array_length = len(copy_array)
    for j in range(array_length):
        swapped = False
        for i in range(array_length - j - 1):
            if comparator(copy_array[i], copy_array[i + 1]) > 0:
                copy_array[i], copy_array[i + 1] = copy_array[i + 1], copy_array[i]
                swapped = True

        if not swapped:
            break

    return copy_array


def selection_sort(input_array, comparator):
    copy_array = input_array[:]
    array_length = len(copy_array)
    for j in range(array_length - 1):
        swap_with = j
        for i in range(j + 1, array_length):
            if comparator(copy_array[i], copy_array[swap_with]) <= 0:
                swap_with = i

        if swap_with != j:
            copy_array[j], copy_array[swap_with] = copy_array[swap_with], copy_array[j]

    return copy_array


def merge_arrays(left, right, comparator):
    left_index = 0
    right_index = 0
    left_length = len(left)
    right_length = len(right)

    result = []
    while left_index < left_length and right_index < right_length:
        if comparator(left[left_index], right[right_index]) <= 0:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left_index < left_length:
        result += left[left_index:]

    if right_index < right_length:
        result += right[right_index:]

    return result


def merge_sort(input_array, comparator):
    array_length = len(input_array)
    if array_length <= 16:
        return selection_sort(input_array, comparator)

    middle = int(array_length / 2)

    left = merge_sort(input_array[:middle], comparator)
    right = merge_sort(input_array[middle:], comparator)

    return merge_arrays(left, right, comparator)


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.func_name, (time2 - time1) * 1000.0))
        return ret

    return wrap


def test_sort(sort_function, comparator, array_size):
    test_time = 0
    test_count = 10
    for i in range(test_count):
        array = [int(10000 * random.random()) for k in range(array_size)]
        time_start = time.time()
        sort_function(array, comparator)
        time_end = time.time()
        test_time += (time_end - time_start)
    print('%s function took %0.3f s' % (sort_function.__name__, test_time / test_count))


if __name__ == "__main__":
    # noinspection PyTypeChecker
    # 8.132 seconds
    test_sort(bubble_sort, ascending_comparator, 10000)
    # noinspection PyTypeChecker
    # 4.701 seconds
    test_sort(selection_sort, ascending_comparator, 10000)
    # noinspection PyTypeChecker
    # 0.026 seconds
    test_sort(merge_sort, ascending_comparator, 10000)



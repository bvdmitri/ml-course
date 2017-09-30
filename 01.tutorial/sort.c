#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>

typedef int (*Comparator)(int a, int b);
typedef int* (*SortFunction)(int *input_array, int length, Comparator comparator);

int ascending_comparator(int a, int b) {
    if (a > b) return 1;
    if (a > b) return 1;
    return 0;
}

void print_array(int *input_array, int length) {
    for (int i = 0; i < length; ++i) {
        printf("%d ", input_array[i]);
    }
    printf("\n");
}

int *bubble_sort(int *input_array, int length, Comparator comparator) {
    int *copy_array = (int *) calloc(length, sizeof(int));
    memcpy(copy_array, input_array, length * sizeof(int));

    for (int j = 0; j < length; ++j) {
        int swapped = 0;
        for (int i = 0; i < length - j - 1; ++i) {
            if (comparator(copy_array[i], copy_array[i + 1]) > 0) {
                int swap_tmp = copy_array[i];
                copy_array[i] = copy_array[i + 1];
                copy_array[i + 1] = swap_tmp;
            }
        }
        if (swapped != 0) break;
    }
    return copy_array;
}

void test_sort(SortFunction function, const char *function_name, Comparator comparator, int array_length) {
    struct timeval  tv;

    double test_time = 0;
    int test_count = 10;

    for (int i = 0; i < test_count; ++i) {
        int *array = (int *) calloc(array_length, sizeof(int));
        for (int k = 0; k < array_length; ++k) {
            array[k] = rand() % 10000;
        }

        gettimeofday(&tv, NULL);
        double time_start = (tv.tv_sec) * 1000 + (tv.tv_usec) / 1000 ;

        int *copy_array = function(array, array_length, comparator);

        gettimeofday(&tv, NULL);
        double time_end = (tv.tv_sec) * 1000 + (tv.tv_usec) / 1000 ;

        test_time += (time_end - time_start);
        free(array);
        free(copy_array);
    }

    printf("%s function took %0.6f ms\n", function_name, test_time / test_count);
}

int main(int argc, char **argv) {
    // 120.9ms
    test_sort(bubble_sort, "bubble_sort", ascending_comparator, 10000);
    return 0;
}
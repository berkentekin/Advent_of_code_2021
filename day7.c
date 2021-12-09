#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "cutils/utils.h"

#define MAXSIZE 10000

long long solve(int* arr);
int cmp(const void *a, const void *b);

int main(int argc, char *argv[])
{
    	FILE *input;
	int crabs[MAXSIZE];

	if (argc != 2) {
		puts("Enter the file loaction");
		exit(EXIT_FAILURE);
	}
	input = fopen(argv[1], "r");
	scan_line(input, crabs, ",");
	printf("%lld\n", solve(crabs));
	exit(EXIT_SUCCESS);

}

int cmp(const void *a, const void *b)
{
	return (*(int*) a - *(int*) b);
}

long long solve(int* arr)
{
	long long total_dist = 0;
	int size = 0;
	double median;

	for (int i = 0; arr[i] != -1; i++) {
		size++;
	}
	qsort(arr, size, sizeof(*arr), cmp);
	/* https://en.wikipedia.org/wiki/Geometric_median */
	median = size % 2 ? (arr[size/2] + arr[(size/2)-1]) / 2 : arr[size/2];
	for (int i = 0; i < size; i++) {
		total_dist += abs((int) median - arr[i]);
	}
	return total_dist;
}

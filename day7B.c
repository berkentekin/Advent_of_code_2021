#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "cutils/utils.h"

#define MAXSIZE 10000

long long solve(int* arr);
double arr_avg(int *arr, int size);

int main(int argc, char *argv[])
{
    	FILE *input;
	int crabs[MAXSIZE];
	if (argc != 2) {
		puts("Enter the file loaction");
		exit(EXIT_FAILURE);
	}
	input = fopen(argv[1], "r");
	scan_file(input, crabs, ",");
	printf("%lld\n", solve(crabs));
	exit(EXIT_SUCCESS);

}

double arr_avg(int *arr, int size) {
    long long sum = 0;
    for (int i = 0; i < size; sum += arr[i++]);
    return sum / (double) size;
    
}

long long solve(int* arr)
{
	long long result = -1, result_cache = 0;
	int size = 0, i;
	long average;

	for (int i = 0; arr[i] != -1; i++) {
		size++;
	}
	average = round(arr_avg(arr, size));
	/*
	  shorturl.at/fCJRU
	 */
	for (long j = average - 1; j <= average + 1; j++) {
	    for (int i = 0; i < size; i++)
		result_cache += (labs(j - arr[i])
			     * (labs(j - arr[i])+1))
		/ 2;
	
	    if (result == -1 || result_cache < result)
		result = result_cache;
	    result_cache = 0;
	}
    
	return result;
}


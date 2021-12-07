#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAXSIZE 10000

void scan_file(FILE *f, int* arr);
long long solve(int* arr);

int main(int argc, char *argv[])
{
    	FILE *input;
	int crabs[MAXSIZE];
	if (argc != 2) {
		puts("Enter the file loaction");
		return EXIT_FAILURE;
	}
	input = fopen(argv[1], "r");
	scan_file(input, crabs);
	printf("%lld\n", solve(crabs));
	return EXIT_SUCCESS;

}

int arr_max(int *arr, int size)
{
	int i, max = arr[0];
	for (i = 0; i < size; i++)
		if (arr[i] > max)
			max = arr[i];
	return max;
}

long long solve(int* arr)
{
	long long result = 0, result_cache = 0;
	int size = 0, i;
	int optimal;

	for (int i = 0; arr[i] != -1; i++) {
		size++;
	}
	/*
	  Brute force approach, using the average didn't work
	*/
	for (optimal = 0; optimal <= arr_max(arr, size); optimal++) {
		for (i = 0; i < size; i++) {
			result_cache += (abs(optimal - arr[i])
					 * (abs(optimal - arr[i])+1))
				/ 2;
		}
		if (result == 0 || result_cache < result)
			result = result_cache;
		result_cache = 0;
	}
    
	return result;
}

void scan_file(FILE *f, int* arr)
{
	unsigned int i;
	char scanfile[MAXSIZE];
	char *tok;

	if (fgets(scanfile, MAXSIZE, f) != NULL) {
		tok = strtok(scanfile, ",");
		for (i = 0; tok != NULL
			     && i < sizeof(scanfile)/sizeof(char);
		     i++) {
			arr[i] = atoi(tok);
			tok = strtok(NULL, ",");
		}
		arr[i] = -1;
	}
	
}

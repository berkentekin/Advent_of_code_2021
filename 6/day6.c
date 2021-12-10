#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cutils/utils.h"
#define BREEDTIME 6
#define NEWBREEDTIME 8
long long solve(int* arr, int days);

int main(int argc, char *argv[])
{
	FILE *input;
	int lanternfish[1000];
	long long solved;
	if (argc != 3) {
		puts("Enter the file loaction and the no. of days");
		return EXIT_FAILURE;
	}
	input = fopen(argv[1], "r");
	scan_line(input, lanternfish, ",");
	solved = solve(lanternfish, atoi(argv[2]));
	printf("%lld\n", solved);
	return EXIT_SUCCESS;
	
}

long long solve(int* arr, int days)
{
	long long no_of_fishes[NEWBREEDTIME+1], result = 0;
	long long temp_0 = 0;
	for (int i = 0; i < NEWBREEDTIME+1; i++)
		no_of_fishes[i] = 0;
	for (int i = 0; arr[i] != -1; i++)
		no_of_fishes[arr[i]]++;
	for (int i = 0; i < days; i++) {
		temp_0 = no_of_fishes[0];
		for (int j = 1; j < NEWBREEDTIME+1; j++)
			no_of_fishes[j-1] = no_of_fishes[j];
		no_of_fishes[NEWBREEDTIME] = temp_0;
		no_of_fishes[BREEDTIME] += temp_0;
	}
	for (int i = 0; i < NEWBREEDTIME+1; i++)
		result += no_of_fishes[i];
	return result;
}


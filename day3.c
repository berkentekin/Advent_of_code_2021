#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	FILE *input;
	int i;
	char arr[13];
	int acc[12] = { 0 }, gamma, epsilon, mask = ~(~0 << 12);
	input = fopen("3_input.txt", "r");
	while (fgets(arr, 13, input)) {
		for (i = 0; arr[i] != 0; i++) {
			switch (arr[i]) {
			case '0':
				acc[i]--;
				break;
			case '1':
				acc[i]++;
				break;
			}
		}
	}
	fclose(input);
	for (i = 0; i < 12; i++) {
		if (acc[i] > 0)
			arr[i] = '1';
		else if (acc[i] < 0)
			arr[i] = '0';
	}
	gamma = strtol(arr, NULL, 2);
	epsilon = gamma ^ mask;
	printf("%d\n", gamma * epsilon);
	return 0;
		
}

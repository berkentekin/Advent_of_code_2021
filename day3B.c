#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define M 13

int main(void)
{
		FILE *input;
		size_t i, j, k;
		int common = 0;
		char arr[M], temp[M], jackpot[M] = { 0 };
		int jp_ind = 0;
		int oxy, co, flag, count = 0;
		input = fopen("3_input.txt", "r");
		for (i = 0; i < M; i++) {
			count = 0;
			for (j = 0; fgets(arr, M, input); j++) {
				flag = 1;
				for (k = 0; k < jp_ind; k++) {
					if (arr[k] != jackpot[k]) {
						flag = 0;
						break;
					}
				}
				
				if (flag == 0) {
					continue;
				}
				else {
					strcpy(temp, arr);
					count++;
					switch (arr[i]) {
					case '0':
						common--;
						break;
					case '1':
						common++;
						break;

					}
				}
			}
			if (count == 1) {
				strcpy(jackpot, temp);
				count = 0;
				rewind(input);
		   		break;
			}
			common = common >= 0 ? 1 : 0;
			jackpot[jp_ind++] = '0' + common;
			common = 0;
			rewind(input);
		}
			
		oxy = strtol(jackpot, NULL, 2);
		jp_ind = 0;
	
		for (i = 0; i < M; i++) {
			count = 0;
			for (j = 0; fgets(arr, M, input); j++) {
				flag = 1;
				for (k = 0; k < jp_ind; k++) {
					if (arr[k] != jackpot[k]) {
						flag = 0;
						break;
					}
				}
				
				if (flag == 0) {
					continue;
				}
				else {
					strcpy(temp, arr);
					count++;
					switch (arr[i]) {
					case '0':
						common--;
						break;
					case '1':
						common++;
						break;

					}
				}
			}
			if (count == 1) {
				strcpy(jackpot, temp);
				count = 0;
				rewind(input);
		   		break;
			}
			common = common >= 0 ? 0 : 1;
			jackpot[jp_ind++] = '0' + common;
			common = 0;
			rewind(input);
		}

		
		
		fclose(input);
		co = strtol(jackpot, NULL, 2);
		printf("%d\n", oxy * co);
		return 0;
		
}

#include <stdio.h>
#include <string.h>
int main(void)
{
		FILE *input;
		long length, hor = 0, ver = 0, aim = 0;
		char direction[8];
		input = fopen("2_input.txt", "r");
		while (fscanf(input, "%s %d", direction, &length) != EOF) {
				if (!strcmp(direction, "forward")) {
						hor += length;
						ver += aim * length;
				}
				else if (!strcmp(direction, "up"))
						aim -= length;
				else if (!strcmp(direction, "down"))
						aim += length;
		}
		fclose(input);
		printf("%ld", hor * ver);
		return 0;
}

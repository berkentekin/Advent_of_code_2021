#include "utils.h"

void scan_file(FILE *f, int* arr, char* delim)
{
	unsigned int i;
	char scanfile[MAXSIZE];
	char *tok;

	if (fgets(scanfile, MAXSIZE, f) != NULL) {
		tok = strtok(scanfile, delim);
		for (i = 0; tok != NULL
			     && i < sizeof(scanfile)/sizeof(char);
		     i++) {
			arr[i] = atoi(tok);
			tok = strtok(NULL, ",");
		}
		arr[i] = -1;
	}
	fclose(f);
	
}
	

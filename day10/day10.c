#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXSCAN 500

int cmpul(const void *a, const void *b) {
	const unsigned long ai = *( const unsigned long* )a;
	const unsigned long bi = *( const unsigned long* )b;
	if (ai < bi)
		return -1;
	if (ai > bi)
		return 1;
	return 0;
}

unsigned long solve1(char** puzzle)
{
	size_t i, j;
	char found;
	char chunk[MAXSCAN], *curr_line, pop;
	int chunk_head = 0;
	unsigned long score = 0;
	for (j = 0; (curr_line = puzzle[j]) != 0; j++) {
		for (i = 0; curr_line[i] != 0; i++) {
			found = 0;
			switch (curr_line[i]) {
			case '(':
			case '[':
			case '{':
			case '<':
				chunk[chunk_head++] = curr_line[i];
				break;
			case ')':
				pop = chunk[--chunk_head];
				if (pop != '(') {
					score += 3;
					found = 1;
				}
				break;
			case ']':
				pop = chunk[--chunk_head];
				if (pop != '[') {
					score += 57;
					found = 1;
				}
				
			        break;
			case '}':
				pop = chunk[--chunk_head];
				if (pop != '{') {
					score += 1197;
					found = 1;
				}
				break;
			case '>':
				pop = chunk[--chunk_head];
				if (pop != '<') {
					score += 25137;
					found = 1;
				}
				break;
			default:
				break;
			}
			if (found) {
				break;
			}
		}
		chunk_head = 0;
	}
	return score;

}


unsigned long solve2(char** puzzle)
{
	size_t i, j;
	char found;
	char chunk[MAXSCAN], *curr_line, pop;
	int chunk_head = 0;
	unsigned long *scores; 
	unsigned long *curr_score;
	int scores_size = 0;
	scores = calloc(1, sizeof(unsigned long));
	
	for (j = 0; (curr_line = puzzle[j]) != 0; j++) {
		found = 0;
		for (i = 0; curr_line[i] != 0; i++) {
			found = 0;
			switch (curr_line[i]) {
			case '(':
			case '[':
			case '{':
			case '<':
				chunk[chunk_head++] = curr_line[i];
				break;
			case ')':
				pop = chunk[--chunk_head];
				chunk[chunk_head] = 0;
				if (pop != '(') {
					found = 1;
				}
				break;
			case ']':
				pop = chunk[--chunk_head];
				chunk[chunk_head] = 0;
				if (pop != '[') {
					found = 1;
				}
				
			        break;
			case '}':
				pop = chunk[--chunk_head];
				chunk[chunk_head] = 0;
				if (pop != '{') {
					found = 1;
				}
				break;
			case '>':
				pop = chunk[--chunk_head];
				chunk[chunk_head] = 0;
				if (pop != '<') {
					found = 1;
				}
				break;
			default:
				break;
			}
			if (found) {
				break;
			}
			
		}
		if (!found) {
			curr_score = &scores[scores_size];
			*curr_score = 0;
			for (; chunk_head >= 0; chunk_head--) {
				*curr_score *= 5;
				switch(chunk[chunk_head]) {
				case '<':
					++*curr_score;
				case '{':
					++*curr_score;
				case '[':
					++*curr_score;
				case '(':
					++*curr_score;
					break;
				}
			}
			scores = realloc(scores, (++scores_size + 1) *
					sizeof(unsigned long));
		}
		chunk_head = 0;
	}
	scores = realloc(scores, scores_size * sizeof(unsigned long));
	qsort(scores, scores_size, sizeof(unsigned long), cmpul);
	return scores[scores_size / 2];
	

}


int main(int argc, char *argv[])
{
	char **scanned_strs, *curr_str;
	FILE *input;
	size_t i;
	if (argc != 2) {
		puts("Type in the location for the input");
		exit(EXIT_FAILURE);
	}
	scanned_strs = calloc(1, sizeof(char*));
	curr_str = calloc(MAXSCAN, sizeof(char));
	input = fopen(argv[1], "r");
	for (i = 0; fgets(curr_str, MAXSCAN, input); i++) {
		scanned_strs = realloc(scanned_strs, (i+1) *
				       sizeof(char*));
		scanned_strs[i] = (char *) strdup(curr_str);
	}
	free(curr_str);
	printf("%lu\n", solve1(scanned_strs));
	printf("%lu\n", solve2(scanned_strs));
	
	exit(EXIT_SUCCESS);
}

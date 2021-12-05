#include <stdio.h>
#define BUFSIZE 3

int main(int argc, char *argv[])
{
  int curr, prev, count = 0;
  int scan_buffer[BUFSIZE+1] = { 0 };
  FILE *input;
  input = fopen("input.txt", "r");
  fscanf(input, "%d", &scan_buffer[0]);
  for (int i = 0; i < BUFSIZE; i++) {
    fscanf(input, "%d", &scan_buffer[i+1]);
  }
  do {
    count += scan_buffer[BUFSIZE] > scan_buffer[0] ? 1 : 0;
    for (int i = 0; i < BUFSIZE; i++) {
      scan_buffer[i] = scan_buffer[i+1];
    }
  }
  while (fscanf(input, "%d", &scan_buffer[BUFSIZE]) != EOF);
  printf("%d\n", count);
  fclose(input);
  return 0;
}

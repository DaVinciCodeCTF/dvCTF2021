#include <stdio.h>
#include <string.h>

void reverse(char *s)
{
  int length, c;
  char *begin, *end, temp;

  length = strlen(s);
  begin  = s;
  end    = s;

  for (c = 0; c < length - 1; c++)
    end++;

  for (c = 0; c < length/2; c++)
  {        
    temp   = *end;
    *end   = *begin;
    *begin = temp;

    begin++;
    end--;
  }
}

int main(int argc, char *argv[]){
  setvbuf(stdout, NULL, _IONBF, 0); /* turn off buffering */
  setvbuf(stdin,  NULL, _IONBF, 0); /* turn off buffering */
  char *secret = "dvCTF{1_h0p3_n01_s33s_th1s}";
  char *output;
  char input[128];

  while(1) {
    printf("Reverse string: ");
    if (fgets(input, sizeof(input), stdin)) {
      reverse(input);
      sprintf(output, input);
      printf("Result: %s\n", output);
    }
  }
}

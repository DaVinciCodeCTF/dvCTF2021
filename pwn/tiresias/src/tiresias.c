#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
	setvbuf(stdin,  NULL, _IONBF, 0); /* turn off buffering */
	setvbuf(stdout, NULL, _IONBF, 0); /* turn off buffering */

	char buffer[128];
	char holder[128];
	int len = 0;

	while (1) {
		printf("\nechOoOoOo\n");

		memset(buffer, 0, sizeof(buffer));
		memset(holder, 0, sizeof(holder));

		if ((len = read(0, buffer, sizeof(buffer))) <= 0) {
			exit(-1);
		}

		if (!strncmp(buffer, "q", 1)) {
			puts("Cya!!");
			exit(0);
		}

		snprintf(holder, sizeof(holder)-1, buffer);
		write(1, holder, strlen(holder));
	}
	return 0;
}

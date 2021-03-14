#include<stdio.h>
#include<string.h>

const char PASSWD[22] = {0x77, 0x41, 0x50, 0x63, 0x55, 0x4c, 0x5a, 0x68, 0x7f, 0x6, 0x78, 0x4, 0x4c, 0x44, 0x64, 0x6, 0x7e, 0x5a, 0x22, 0x59, 0x74, 0x4a};

int transform(char * input) {
	char * new;
	for (int i = 0; i < strlen(PASSWD); i++) {
		if (i % 2 == 0) {
			new[i] = input[i] ^ 0x13;
		} else {
			new[i] = input[i] ^ 0x37;
		}
	}
	return strncmp(PASSWD, new, 22);
}

int main(int argc, char *argv[]) {
	if (argc == 2) {
		int result = transform(argv[1]);
		if (!result) {
			puts("Nice flag");
		} else {
			puts("Nice try");
		}
	} else {
		printf("Usage: %s <password>\n", argv[0]);
		return 1;
	}

	return 0;

}

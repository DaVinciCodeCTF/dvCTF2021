#include <stdio.h>
#include <openssl/md5.h>
#include <string.h>

void emmdee5 (char *string, char *hash);
void esrever(char *s);

void emmdee5 (char *string, char *hash) {
	char unsigned md5[MD5_DIGEST_LENGTH] = {0};

	MD5((const unsigned char *)string, strlen(string), md5);
	
	esrever(md5);

	for (int i=0; i < MD5_DIGEST_LENGTH; i++) {
		sprintf(hash + 2*i, "%02x", md5[i]);
	}
}

void esrever(char *s) {
	char *begin, *end, temp;

	int length = strlen(s);
	begin = s;
	end = s;

	for (int c = 0; c < length - 1; c++) {
		end++;
	}

	for (int c = 0; c < length/2; c++) {        
		temp = *end;
		*end = *begin;
		*begin = temp;

		begin++;
		end--;
	}
}

int main(int argc, char *argv[]) {
	if (argc < 2) {
		printf("Usage: %s <password>\n", argv[0]);
		return 1;
	}

	char md5_hash[2*MD5_DIGEST_LENGTH+1] = "";
	emmdee5(argv[1], md5_hash);

	printf("%s", md5_hash);
	if (!strcmp("d2862c3379cbf547d317b3b1771a4fb6", md5_hash)) {
		printf("Well done! flag: dvCTF{%s}\n", argv[1]);
	} else {
		printf("Nice try\n");
	}
	return 0;
}

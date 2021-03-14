#include <stdio.h>
#include <stdlib.h>

void recovery_mode() {
	system("cat  ./flag");
}

void submit_ticket() {
	// Do nothing, lol
	printf("Our security team will reply as soon as possible.\n");
}

int main() {
	setvbuf(stdout, NULL, _IONBF, 0); /* turn off buffering */
	setvbuf(stdin,  NULL, _IONBF, 0); /* turn off buffering */
	void (*submit)()=submit_ticket;
	char email[40];
	char message[1024];
	printf("Ticket submission service\n");
	printf("Email: ");
	fgets(email, 45, stdin);
	printf("Message: ");
	fgets(message, 1024, stdin);
	submit();
	return 0;
}

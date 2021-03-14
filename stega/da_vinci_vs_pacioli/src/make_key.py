import random
void = bytes(range(256))
repeat = 2510000
repeat += random.randint(1, 150)
password = b'sup4_dup4_p4ssw0rd_4m4z1ng_n01_w1ll_susp3ct'
with open('nothing_to_see_here', 'wb') as key:
    key.write(void * repeat)
    key.write(password.hex().encode())
    key.write(void * repeat)

import json

def generate_RSA_key_pair(N):
    n = 0
    p = 0
    q = 0
    """Repeat until n has length N because multiplying two numbers of length N/2 can result in n of length N-1"""
    while n.nbits() != 1024:
        p = random_prime(2^(N//2), lbound = 2^(N//2 -1))
        q = random_prime(2^(N//2), lbound = 2^(N//2 -1))
        n = p*q
    return n

N = generate_RSA_key_pair(1024)
e = 3

flag = b'dvCTF{RS4_m0dul0_inf1nity}'
flag = int(flag.hex(), 16)

ct = power_mod(flag, e, N)

challenge = {"N": int(N), "e": int(e), "ct": int(ct)}

print(challenge)

with open("supersecret.json", 'w') as output:
    output.write(json.dumps(challenge))

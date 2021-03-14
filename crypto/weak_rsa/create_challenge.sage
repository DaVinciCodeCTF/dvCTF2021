import json
from sage.crypto.util import random_blum_prime

p = random_blum_prime(2**127, 2**129)
q = random_blum_prime(2**127, 2**129)

N = p*q

e = 0x10001

flag = b'dvCTF{rs4_f4ctor1z4t10n!!!}'
flag = int(flag.hex(), 16)

print(flag, Integer(flag).nbits())

ct = pow(flag, e, N)

challenge = {"N": int(N), "e": int(e), "ct": int(ct)}

print(challenge)

with open("weak_rsa.json", 'w') as output:
    output.write(json.dumps(challenge))

import json

primes = [random_prime(2^32-1, false, 2^31) for i in range(32)]

N = prod(primes)

e = 65537

flag = b'dvCTF{rs4_f4ctor1z4t10n!!!}'
flag = int(flag.hex(), 16)

ct = pow(flag, e, N)

challenge = {"N": int(N), "e": int(e), "ct": int(ct)}

print(challenge)

with open("supersecret.json", 'w') as output:
    output.write(json.dumps(challenge))

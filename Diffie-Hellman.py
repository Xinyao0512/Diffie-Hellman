# diffie_hellman.py

import random

# 模幂计算函数（快速幂）
def mod_exp(base, exponent, mod):
    result = 1
    base %= mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent //= 2
        base = (base * base) % mod
    return result

# 公共参数（素数 p 和原根 g）
p = 23      # 模数（公开素数）
g = 5       # 原根（基）

print(f"公共参数: p = {p}, g = {g}")

# Alice 私钥（随机选取）
a = random.randint(2, p-2)
A = mod_exp(g, a, p)
print(f"Alice 选择的私钥 a = {a}")
print(f"Alice 计算并发送 A = g^a mod p = {A}")

# Bob 私钥（随机选取）
b = random.randint(2, p-2)
B = mod_exp(g, b, p)
print(f"Bob 选择的私钥 b = {b}")
print(f"Bob 计算并发送 B = g^b mod p = {B}")

# 交换公钥后，各自计算共享密钥
shared_key_alice = mod_exp(B, a, p)
shared_key_bob = mod_exp(A, b, p)

print(f"\nAlice 计算共享密钥: (B^a) mod p = {shared_key_alice}")
print(f" Bob   计算共享密钥: (A^b) mod p = {shared_key_bob}")

# 验证结果是否一致
if shared_key_alice == shared_key_bob:
    print(f"\n成功！共享密钥为: {shared_key_alice}")
else:
    print("\n共享密钥计算失败，不一致！")

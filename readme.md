
# 🛡️ Diffie-Hellman 密钥交换算法实现实验

本项目实现了一个基于 Python 的 Diffie-Hellman 密钥交换算法，适用于信息安全导论课程教学与实验。

## 🔐 算法原理简介

Diffie-Hellman 密钥交换算法由 Whitfield Diffie 和 Martin Hellman 于 1976 年提出，是第一个实用的公开密钥协议。

### 📌 基本思想：

1. **双方公开一个大素数 p 和其原根 g**（g 是模 p 下的生成元）。
2. **Alice 随机选择私钥 a**，计算 A = g^a mod p。
3. **Bob 随机选择私钥 b**，计算 B = g^b mod p。
4. 双方交换 A 和 B。
5. **Alice 使用 Bob 的 B，计算共享密钥 K = B^a mod p**。
6. **Bob 使用 Alice 的 A，计算共享密钥 K = A^b mod p**。
7. 根据模运算性质，有 B^a ≡ A^b ≡ g^(ab) mod p，因此 Alice 和 Bob 得到相同的共享密钥 K。

> ✅ 整个过程中，私钥 a 和 b 从未在网络上传输，因此是安全的。

---

## 📁 文件说明

- `diffie_hellman.py`：主程序，模拟 Alice 和 Bob 的密钥交换过程，输出生成的共享密钥。

---

## ▶️ 运行方式

确保你已安装 Python 3，在终端中运行：

```bash
python diffie_hellman.py
```

输出将显示每一步的私钥、公钥、共享密钥，验证共享密钥是否一致。

---

## 📚 教学价值

- 了解公开密钥交换的基本思想；
- 熟悉快速幂算法、模运算在密码学中的应用；
- 掌握共享密钥如何通过不对称运算达成对称加密基础。


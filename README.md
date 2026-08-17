# 🔐 Password Auditor & Cryptography Demo Tool

A Python CLI application designed to analyze password strength (entropy calculations), demonstrate fast unsalted hash vulnerabilities (MD5, SHA-256, SHA-512), showcase secure password storage using key stretching (Salted PBKDF2-HMAC-SHA256), and perform educational dictionary lookup attacks using common wordlists (`rockyou.txt`).

---

## ✨ Features

- **📊 Strength & Entropy Analysis**: Calculates mathematical information entropy ($E = L \times \log_2(N)$) based on character set pool size and flags dictionary passwords.
- **⚡ Multi-Algorithm Hash Suite**: Computes fast unsalted cryptographic digests (`MD5`, `SHA-256`, `SHA-512`).
- **🛡️ Secure Password Hashing**: Implements `PBKDF2-HMAC-SHA256` with random 16-byte salting and 100,000 key-stretching iterations.
- **🎲 Strong Password Generator**: Generates 100+ bit entropy cryptographically secure passwords.
- **🔍 Dictionary Lookup Demo**: Searches wordlists (`rockyou.txt`) to demonstrate hash cracking vulnerabilities against fast, unsalted algorithms.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+** (Uses standard library modules: `hashlib`, `math`, `re`, `secrets`, `os`, `sys`).
- A text wordlist such as `rockyou.txt` placed in the project root directory.

### Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/FogProtocol/password-auditor.git
   cd password-auditor

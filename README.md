# 🔐 Password Auditor & Cryptography Demo Tool

A comprehensive Python CLI application designed to analyze password strength via information entropy, demonstrate fast unsalted hash vulnerabilities (MD5, SHA-256, SHA-512), showcase secure password storage using key stretching (Salted PBKDF2-HMAC-SHA256), and execute dictionary lookup attacks using `rockyou.txt`.

---

## 🔍 What is Password Auditing & Cryptography?

Password auditing evaluates credential security to defend against dictionary attacks and unauthorized access:

- 📊 **Information Entropy**: Measures password randomness in bits ($E = L \times \log_2(N)$). Higher entropy means exponential brute-force difficulty.
- ⚡ **Unsalted Fast Hashes**: Demonstrates how legacy hash algorithms (MD5, SHA-256) can be cracked in seconds via pre-computed lookup tables.
- 🛡️ **Salted Key Stretching**: Demonstrates modern secure storage (`PBKDF2`) using 16-byte random salts and 100,000 computation rounds.
- 🔍 **Dictionary Attack Demo**: Tests target hashes against `rockyou.txt` to highlight the vulnerability of common passwords.

---

## ⚙️ Features & Cryptographic Engine

All checks and hash functions follow industry security standards:

| Feature / Module | Description |
| :--- | :--- |
| **Entropy Calculation** | Computes exact mathematical entropy based on character set pool size (lowercase, uppercase, digits, symbols). |
| **Wordlist Detection** | Flags inputs that appear in common credential lists like `rockyou.txt`. |
| **Multi-Hash Suite** | Computes raw digests for `MD5`, `SHA-256`, and `SHA-512` simultaneously. |
| **Salted PBKDF2** | Generates secure 16-byte salted hashes stretched across 100,000 iterations. |
| **Strong Password Generator** | Produces cryptographically secure 16+ character passwords with $>100$ bits of entropy. |
| **Dictionary Lookup Engine** | Iterates through `rockyou.txt` to crack unsalted MD5/SHA-256/SHA-512 hashes. |

---

## 📁 Project Structure

```text
password-auditor/
├── analyzer.py   # Entropy math, character pool scoring & wordlist detection
├── hasher.py     # Hash algorithms, PBKDF2 salting & dictionary cracking engine
├── main.py       # Interactive CLI menu interface with plain-text explanations
├── .gitignore    # Excludes large wordlists (rockyou.txt) and cache files
├── LICENSE       # MIT License
└── README.md     # Documentation file
```

---

## 🚀 Installation & Usage

### ✅ Requirements
- **Python 3.8+**
- **Git**
- A wordlist such as `rockyou.txt` placed in the project root directory.

---

### 📥 Step 1 — Clone the Repository
```bash
git clone https://github.com/FogProtocol/password-auditor.git
cd password-auditor
```

---

### 📦 Step 2 — Add Wordlist
Place `rockyou.txt` inside your project folder.

---

### ▶️ Step 3 — Run the Auditor
```bash
python main.py
```

---

### 📊 Step 4 — Select Menu Option

Upon running `main.py`, choose from the interactive menu:
1. **Option 1**: Comprehensive Audit (Entropy + Multi-Hashes + Strong Password Recommendation).
2. **Option 2**: Generate Multi-Algorithm Hashes Only.
3. **Option 3**: Run Educational Dictionary Lookup Demo against `rockyou.txt`.

---

## 🛠️ Built With
- **Python 3**
- **Cryptography Standard Modules (`hashlib`, `secrets`, `math`, `re`)**

---

## 👤 Author
- **Gagan H S**
- GitHub: [@FogProtocol](https://github.com/FogProtocol)

---

## 📜 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer
*This project is built strictly for **educational and defensive security training purposes**. It should only be used to test password strength and audit security awareness.*

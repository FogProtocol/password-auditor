import hashlib
import os
import secrets
import string

class PasswordHasher:
    @staticmethod
    def hash_md5(text):
        """Generates an unsalted MD5 hash (Legacy/Insecure)."""
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    @staticmethod
    def hash_sha256(text):
        """Generates an unsalted SHA-256 hash (Fast hash)."""
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

    @staticmethod
    def hash_sha512(text):
        """Generates an unsalted SHA-512 hash (512-bit output)."""
        return hashlib.sha512(text.encode('utf-8')).hexdigest()

    @staticmethod
    def hash_pbkdf2_sha256(password, salt=None, iterations=100000):
        """Generates a secure PBKDF2-HMAC-SHA256 hash with salting and key stretching."""
        if salt is None:
            salt = os.urandom(16)
        
        derived_key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            iterations
        )
        return {
            "hash": derived_key.hex(),
            "salt": salt.hex(),
            "iterations": iterations
        }

    @staticmethod
    def generate_strong_password(length=16):
        """Generates a cryptographically secure random password."""
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        while True:
            password = ''.join(secrets.choice(alphabet) for _ in range(length))
            # Ensure it contains uppercase, lowercase, digits, and special characters
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and any(c.isdigit() for c in password)
                    and any(c in "!@#$%^&*" for c in password)):
                return password

    @staticmethod
    def dictionary_lookup_demo(target_hash, hash_algo, wordlist_path):
        """Demonstrates dictionary lookup against unsalted fast hashes."""
        algo_map = {
            "md5": PasswordHasher.hash_md5,
            "sha256": PasswordHasher.hash_sha256,
            "sha512": PasswordHasher.hash_sha512
        }

        if hash_algo.lower() not in algo_map:
            return {"found": False, "error": f"Unsupported algorithm '{hash_algo}'"}

        hash_func = algo_map[hash_algo.lower()]
        target_hash = target_hash.strip().lower()

        try:
            attempts = 0
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    candidate = line.strip()
                    if not candidate:
                        continue
                    attempts += 1
                    if hash_func(candidate) == target_hash:
                        return {
                            "found": True,
                            "match": candidate,
                            "attempts": attempts
                        }
            return {"found": False, "attempts": attempts}
        except FileNotFoundError:
            return {"found": False, "error": f"Wordlist file '{wordlist_path}' not found."}

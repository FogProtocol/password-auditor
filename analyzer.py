import math
import re

class PasswordAnalyzer:
    def __init__(self, wordlist_path=None):
        self.common_passwords = set()
        if wordlist_path:
            self.load_wordlist(wordlist_path)

    def load_wordlist(self, filepath):
        """Loads common passwords from a text file into a set."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                self.common_passwords = {line.strip() for line in f if line.strip()}
        except FileNotFoundError:
            print(f"[!] Warning: Wordlist file '{filepath}' not found.")

    def calculate_entropy(self, password):
        """
        Calculates information entropy (in bits) based on character set pool size.
        Formula: E = Length * log2(Pool Size)
        """
        if not password:
            return 0.0

        pool_size = 0
        if re.search(r'[a-z]', password):
            pool_size += 26
        if re.search(r'[A-Z]', password):
            pool_size += 26
        if re.search(r'[0-9]', password):
            pool_size += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            pool_size += 32  # Standard special character pool

        if pool_size == 0:
            return 0.0

        entropy = len(password) * math.log2(pool_size)
        return round(entropy, 2)

    def evaluate_strength(self, password):
        """Evaluates overall password strength and checks dictionary status."""
        entropy = self.calculate_entropy(password)
        is_common = password in self.common_passwords

        # Categorize entropy levels
        if entropy < 28:
            rating = "Very Weak"
        elif entropy < 36:
            rating = "Weak"
        elif entropy < 60:
            rating = "Reasonable"
        elif entropy < 128:
            rating = "Strong"
        else:
            rating = "Very Strong"

        feedback = []
        if is_common:
            rating = "Extremely Vulnerable (Found in Wordlist!)"
            feedback.append("This password appears in common wordlists and can be instantly compromised.")

        if len(password) < 12:
            feedback.append("Increase length to at least 12-16 characters.")
        if not re.search(r'[A-Z]', password):
            feedback.append("Include uppercase letters.")
        if not re.search(r'[0-9]', password):
            feedback.append("Include numeric digits.")
        if not re.search(r'[^a-zA-Z0-9]', password):
            feedback.append("Include special symbols (!@#$%^&*).")

        return {
            "password": password,
            "length": len(password),
            "entropy_bits": entropy,
            "rating": rating,
            "is_in_wordlist": is_common,
            "feedback": feedback
        }

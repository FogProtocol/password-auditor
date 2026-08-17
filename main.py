import sys
from analyzer import PasswordAnalyzer
from hasher import PasswordHasher

def print_banner():
    print("\n" + "=" * 65)
    print("      PASSWORD STRENGTH ANALYZER & CRYPTO DEMO TOOL      ")
    print("=" * 65)

def display_hash_suite(pwd):
    """Prints hashes across MD5, SHA-256, SHA-512, and PBKDF2."""
    md5_res = PasswordHasher.hash_md5(pwd)
    sha256_res = PasswordHasher.hash_sha256(pwd)
    sha512_res = PasswordHasher.hash_sha512(pwd)
    pbkdf2_res = PasswordHasher.hash_pbkdf2_sha256(pwd)

    print(f"\n--- HASH SUITE FOR: '{pwd}' ---")
    print(f"MD5 (Insecure)     : {md5_res}")
    print(f"SHA-256 (Fast)     : {sha256_res}")
    print(f"SHA-512 (Fast)     : {sha512_res}")
    print(f"Salted PBKDF2-SHA256:")
    print(f"  Salt (Hex)       : {pbkdf2_res['salt']}")
    print(f"  Hash (Hex)       : {pbkdf2_res['hash']}")
    print(f"  Iterations       : {pbkdf2_res['iterations']}")

def main():
    wordlist_path = "rockyou.txt"
    analyzer = PasswordAnalyzer(wordlist_path)

    while True:
        print_banner()
        print("1. Comprehensive Audit (Strength + Hashes + Strong Recommendation)")
        print("2. Generate Multi-Algorithm Hashes Only")
        print("3. Run Educational Dictionary Lookup Demo")
        print("4. Exit")
        print("-" * 65)
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            pwd = input("\nEnter a password to audit: ")
            res = analyzer.evaluate_strength(pwd)
            
            print("\n" + "=" * 40)
            print("         STRENGTH ANALYSIS")
            print("=" * 40)
            print(f"Password        : {res['password']}")
            print(f"Length          : {res['length']}")
            print(f"Entropy         : {res['entropy_bits']} bits")
            print(f"Strength Rating : {res['rating']}")
            print(f"In Wordlist?    : {'YES' if res['is_in_wordlist'] else 'No'}")
            
            if res['feedback']:
                print("\nRecommendations:")
                for fb in res['feedback']:
                    print(f" - {fb}")

            # Generate hashes for entered password
            display_hash_suite(pwd)

            # Generate a strong password recommendation
            strong_rec = PasswordHasher.generate_strong_password(16)
            strong_eval = analyzer.evaluate_strength(strong_rec)

            print("\n" + "=" * 40)
            print("   RECOMMENDED STRONG ALTERNATIVE")
            print("=" * 40)
            print(f"Suggested Password : {strong_rec}")
            print(f"Entropy            : {strong_eval['entropy_bits']} bits")
            print(f"Rating             : {strong_eval['rating']}")
            
            display_hash_suite(strong_rec)

        elif choice == "2":
            pwd = input("\nEnter text/password to hash: ")
            display_hash_suite(pwd)

        elif choice == "3":
            print("\n--- DICTIONARY LOOKUP DEMO ---")
            algo = input("Enter algorithm (md5 / sha256 / sha512): ").strip()
            target_hash = input("Enter target hash string: ").strip()
            
            print(f"Searching wordlist '{wordlist_path}'...")
            result = PasswordHasher.dictionary_lookup_demo(target_hash, algo, wordlist_path)
            
            if result.get("error"):
                print(f"[!] Error: {result['error']}")
            elif result["found"]:
                print(f"[+] Match found! Word: '{result['match']}' (after {result['attempts']} attempts)")
            else:
                print(f"[-] No match found in wordlist after {result['attempts']} attempts.")

        elif choice == "4":
            print("Exiting tool. Goodbye!")
            sys.exit(0)

        else:
            print("[!] Invalid option. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

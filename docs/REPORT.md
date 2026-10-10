# Password Security & Authentication Research Report

## 1. Common Password Attacks
- **Brute Force Attack:** Attackers use automated tools to try every possible combination of characters until they guess the correct password.
- **Dictionary Attack:** Attackers use a predefined list of common words, phrases, and leaked passwords (a "dictionary") to systematically test against an account.
- **Credential Stuffing:** Attackers take lists of leaked username/password pairs from previous breaches on other sites and automatedly try them on multiple other platforms, exploiting the fact that users reuse passwords.

## 2. Hashing vs. Encryption

| Feature | Cryptographic Hashing | Encryption |
| :--- | :--- | :--- |
| **Type** | One-Way Function (Cannot be reversed) | Two-Way Function (Can be decrypted) |
| **Purpose** | Verifying data integrity and password storage | Secure data transmission and communication |
| **Key Requirement** | No key required (Uses algorithms like bcrypt) | Requires a secret key (Public/Private or Symmetric) |
| **Primary Use Case** | Storing user credentials securely in databases | Protecting confidential messages, files, or network traffic |

## 3. Password Strength Matrix

| Weak Passwords (Dangerous) | Strong Passwords (Secure) |
| :--- | :--- |
| Short length (less than 8 characters) | Minimum 12-16 characters in length |
| Contains common words, names, or sequential numbers (e.g., `password123`, `12345678`) | Mix of uppercase letters, lowercase letters, numbers, and special symbols (e.g., `@`, `#`, `$`) |
| Reused across multiple different websites | Unique password for every single account |
| Uses predictable substitutions (e.g., replacing `E` with `3`) | Randomly generated strings or long multi-word passphrases |

## 4. Security Recommendations
1. **Enforce Salted Hashing:** Never store plaintext passwords. Always use slow, salted cryptographic algorithms like `bcrypt` or `Argon2` to defend against rainbow table lookups.
2. **Implement Rate Limiting:** Prevent brute force attacks by temporarily blocking or slowing down IP addresses after multiple failed login attempts.
3. **Mandate Multi-Factor Authentication (MFA):** Add a secondary verification layer (like SMS TOTP or Authenticator apps) so that even if a password is stolen, the account remains protected.

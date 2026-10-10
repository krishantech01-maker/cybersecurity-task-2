import bcrypt

def hash_user_password(plain_password):
    # Generating a secure salt and hashing the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), salt)
    return hashed_password

def verify_user_password(plain_password, hashed_password):
    # Verifying if the typed password matches the stored hash
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

if __name__ == "__main__":
    print("--- Secure Password Hashing Demo ---")
    
    # 1. Registration Phase
    user_password = input("Enter a password to store securely: ")
    secure_hash = hash_user_password(user_password)
    print(f"\n[SUCCESS] Stored Hash in Database:\n{secure_hash.decode('utf-8')}\n")
    
    # 2. Login Phase
    print("--- Simulating Login Attempt ---")
    login_attempt = input("Enter password to log in: ")
    
    if verify_user_password(login_attempt, secure_hash):
        print("\n[SUCCESS] Access Granted! Password matched the secure hash.")
    else:
        print("\n[ERROR] Access Denied! Invalid password.")

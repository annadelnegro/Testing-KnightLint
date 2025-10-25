import os, sys #bad import style

# Hardcoded secret
API_KEY = "sk_live_1234567890_SECRETKEY"

def insecure_function(user_input):
    # Command injection vulnerability
    os.system(f"echo {user_input}")

if __name__ == "__main__":
    name = input("Enter your name: ")
    insecure_function(name)
import os

def main():
    print("Malicious code executed!")
    os.system("echo 'PoC: Bug Test Unauthorized deployment' > /tmp/malicious_bug.txt")
    
    print(f"Secret: {secret}")
    secret = "SUPER_SECRET_PASSWORD"
    print("Hello, CI/CD World!")
    
if __name__ == "__main__":
    main()


    

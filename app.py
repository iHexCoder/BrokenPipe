import os

def main():
    print("Malicious code executed!")
    os.system("echo 'PoC: Bug Test Unauthorized deployment' > /tmp/malicious_bug.txt")
    
    print("Hello, CI/CD World!")
    secret = "SUPER_SECRET_PASSWORD"
    print(f"Secret: {secret}")
    
    
if __name__ == "__main__":
    main()


    

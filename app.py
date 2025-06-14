import os

def main():
    print("Malicious code executed!")
    os.system("echo 'PoC: Bug Test Unauthorized deployment' > /tmp/malicious_bug.txt")
    print("Kept Kalm Myself And Hacked Your Infra just using an CI/CD Pipeline")
    print("Tell Your Infra Boss that 0xOffensiveHex was here... and also tell your friends that update the pipeline...")
        
    secret = "SUPER_SECRET_PASSWORD"
    print(f"Secret: {secret}")
    
    
if __name__ == "__main__":
    main()


    

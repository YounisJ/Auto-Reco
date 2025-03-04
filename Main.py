import subprocess
import pyfiglet
import os
import re
from tqdm import tqdm
from termcolor import colored


# Display banner
banner = pyfiglet.figlet_format("Auto Recon !!!")
print(colored(banner, "cyan"))

print(colored("\n\nThis tool is built for pentesters and bug hunters You \njust have to provide the URL of the website you want to\nperform reconnesance on", "blue"))

# Get user input
url = input(colored("\nEnter Website URL Please: ", "yellow")).strip()

# Create output directory
output_dir = f"Auto_Recon_For_{url}"
os.makedirs(output_dir, exist_ok=True)



# Function to run a command and return output
def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(colored(f"[!] Error running {command[0]}: {e}", "red"))
        return None

# Step 1: Collecting Subdomains Using Subfinder
print(colored("\n[+] Running Subfinder to collect subdomains...", "blue"))

subfinder_output = run_command(["subfinder", "-d", url])
if subfinder_output:
    subdomains = subfinder_output.split("\n")
    subdomains = [s.strip() for s in subdomains if s.strip()]
    output_file = os.path.join(output_dir, "SubDomains.txt")

    with open(output_file, "w") as f:
        f.write("\n".join(subdomains))

    print(colored(f"[✓] Subdomains saved in: {output_file}", "green"))
else:
    print(colored("[!] No subdomains found or Subfinder failed.", "red"))

# Step 2: Scanning Open Ports with Nmap
print(colored("\n[+] Running Nmap to check open ports...", "blue"))



nmap_output = run_command(["nmap", "-sV", url])
if nmap_output:
    output_file = os.path.join(output_dir, "NmapResult.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(nmap_output + "\n")

    print(colored(f"[✓] Nmap result saved in: {output_file}", "green"))
else:
    print(colored("[!] Nmap scan failed.", "red"))

print(colored("\n[✓] Recon completed successfully!", "green"))

# Step 3: 





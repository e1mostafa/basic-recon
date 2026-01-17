import requests
import sys

def get_subdomains(domain):
    print(f"\n[+] Searching crt.sh for subdomains of: {domain}")
    
    # URL for crt.sh requesting JSON output
    url = f"https://crt.sh/?q=%.{domain}&output=json"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"[-] Error fetching data: Status {response.status_code}")
            return

        data = response.json()
        subdomains = set() # Use a set to automatically handle duplicates

        for entry in data:
            name_value = entry['name_value']
            # Sometimes name_value contains multiple domains separated by newlines
            lines = name_value.split('\n')
            for line in lines:
                if '*' not in line: # Remove wildcards like *.example.com
                    subdomains.add(line)

        # Sort and Print
        print(f"\n[+] Found {len(subdomains)} unique subdomains:")
        for sub in sorted(subdomains):
            print(sub)

    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_domain = sys.argv[1]
    else:
        target_domain = input("Enter domain (e.g., google.com): ")
    
    get_subdomains(target_domain)
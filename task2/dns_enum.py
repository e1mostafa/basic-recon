import dns.resolver
import sys

def get_dns_records(domain):
    print(f"\n[+] Enumerating DNS records for: {domain}")
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
    
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n--- {record} Records ---")
            for rdata in answers:
                print(rdata.to_text())
        except dns.resolver.NoAnswer:
            # Record type exists generally, but not for this specific domain
            pass 
        except dns.resolver.NXDOMAIN:
            print(f"[-] Domain {domain} does not exist.")
            break
        except Exception as e:
            print(f"[-] Could not fetch {record}: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_domain = sys.argv[1]
    else:
        target_domain = input("Enter domain (e.g., google.com): ")
    
    get_dns_records(target_domain)
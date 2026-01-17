import dns.resolver

def enumerate_dns(domain):
    print(f"\n[*] Enumerating DNS for: {domain}")
    print("-" * 40)

    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']

    for record in record_types:
        print(f"\n[+] {record} Records:")
        try:
            answers = dns.resolver.resolve(domain, record)
            
            for answer in answers:
                print(f"    {answer.to_text()}")
                
        except dns.resolver.NoAnswer:
            print(f"    [!] No {record} record found.")
        except dns.resolver.NXDOMAIN:
            print(f"    [!] Domain '{domain}' does not exist.")
            return 
        except dns.resolver.Timeout:
            print("    [!] Request timed out.")
        except Exception as e:
            print(f"    [!] Error: {e}")

if __name__ == "__main__":
    target_domain = input("Enter Target Domain (e.g., google.com): ")
    enumerate_dns(target_domain)
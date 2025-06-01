def check_acls(conn, users, groups):
    issues = []
    print("[*] ACL kontrolleri yapılıyor...")

    for group in groups:
        members = group.get('member', [])
        if not members:
            continue

        for member in members:
            if 'Domain Admins' in group['cn']:
                if 'svc' in member.lower():  # servis hesabı domain admin mi?
                    issues.append({
                        'type': 'ACL',
                        'group': group['cn'],
                        'member': member,
                        'issue': 'Servis hesabı Domain Admin grubunda!'
                    })
                    print(f"[!] Servis hesabı Domain Admin: {member}")

    return issues

from ldap3 import Server, Connection, ALL

def connect_to_ad(server_ip='192.168.1.100', user='user@domain.local', password='Passw0rd'):
    server = Server(server_ip, get_info=ALL)
    conn = Connection(server, user, password, auto_bind=True)
    print(f"[+] Bağlantı başarılı: {server_ip}")
    return conn

def get_users(conn):
    conn.search('dc=domain,dc=local', '(objectClass=user)', attributes=['cn', 'memberOf'])
    users = [entry['attributes'] for entry in conn.entries]
    print(f"[+] {len(users)} kullanıcı bulundu.")
    return users

def get_groups(conn):
    conn.search('dc=domain,dc=local', '(objectClass=group)', attributes=['cn', 'member'])
    groups = [entry['attributes'] for entry in conn.entries]
    print(f"[+] {len(groups)} grup bulundu.")
    return groups

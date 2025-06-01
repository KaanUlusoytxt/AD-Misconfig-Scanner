import json
import os
from datetime import datetime

def generate_report(acl_issues, roastable_accounts):
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = os.path.join('reports', f'report_{timestamp}.json')

    report_data = {
        'timestamp': timestamp,
        'acl_issues': acl_issues,
        'kerberoast_accounts': roastable_accounts
    }

    os.makedirs('reports', exist_ok=True)
    with open(report_path, 'w') as f:
        json.dump(report_data, f, indent=4)

    print(f"[+] Rapor kaydedildi: {report_path}")

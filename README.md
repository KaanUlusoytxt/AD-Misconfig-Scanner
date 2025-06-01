# AD Misconfiguration Scanner

Active Directory (AD) ortamlarındaki yanlış yapılandırmaları ve güvenlik açıklarını tespit etmek için geliştirilmiş bir Python tabanlı tarama aracıdır.

---

## Özellikler

- AD sunucusuna bağlanarak kullanıcı ve grup bilgilerini toplar  
- Domain Admins grubunda riskli servis hesaplarını tespit eder  
- Kerberoast için hedef olabilecek servis hesaplarını bulur  
- Bulunan güvenlik sorunlarını JSON formatında raporlar

---

## Gereksinimler

- Python 3.8+  
- [ldap3](https://pypi.org/project/ldap3/)  
- [impacket](https://github.com/SecureAuthCorp/impacket) (Kerberoasting için)  

`requirements.txt` dosyasındaki paketler kurulmalıdır.

---

## Kurulum

```bash
pip install -r requirements.txt

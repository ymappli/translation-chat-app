from OpenSSL import crypto
import os

def generate_self_signed_cert():
    # Générer la clé
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Générer le certificat
    cert = crypto.X509()
    cert.get_subject().C = "FR"
    cert.get_subject().ST = "France"
    cert.get_subject().L = "Paris"
    cert.get_subject().O = "Translation Chat App"
    cert.get_subject().OU = "Development"
    cert.get_subject().CN = "localhost"

    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(365*24*60*60)  # Valide pour un an
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')

    # Écrire le certificat et la clé
    with open("cert.pem", "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
    with open("key.pem", "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

if __name__ == '__main__':
    generate_self_signed_cert()

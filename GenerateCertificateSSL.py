#!/usr/bin/env python
from OpenSSL import crypto

key = crypto.PKey()
key.generate_key(crypto.TYPE_RSA, 2048)
cert = crypto.X509()
cert.get_subject().CN = "localhost"
cert.get_subject().O = 'localhost.local'
cert.get_subject().OU = 'localhost'
cert.get_subject().L = 'local'
cert.get_subject().ST = 'Spain'
cert.get_subject().C = 'ES'
cert.get_subject().emailAddress = 'test@localhost.local'
subject = cert.get_subject()
cert.set_serial_number(666)
#-10*365*24*60*60
cert.gmtime_adj_notBefore(0)
cert.gmtime_adj_notAfter(20*365*24*60*60)
cert.set_issuer(cert.get_subject())
cert.set_pubkey(key)
cert.sign(key, 'sha256')


req = crypto.X509Req()
req.get_subject().CN = "localhost"
req.get_subject().O = 'localhost.local'
req.get_subject().OU = 'localhost'
req.get_subject().L = 'local'
req.get_subject().ST = 'Spain'
req.get_subject().C = 'ES'
req.get_subject().emailAddress = 'ztest@localhost.local'
req.set_pubkey(key)
req.sign(key, "sha256")

open("test.key", "wb").write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
open("test.crs", "wb").write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))
open("test.crt", "wb").write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

#!/usr/bin/python
from OpenSSL import crypto
import os
import sys
import datetime


#Variables
TYPE_RSA = crypto.TYPE_RSA
TYPE_DSA = crypto.TYPE_DSA
HOME = os.getenv("HOME")
now = datetime.datetime.now()
d = now.date()

#Pull these out of scope
cn = raw_input("Enter the Domain: ")
key = crypto.PKey()
keypath = HOME + "/" + cn + '-' + str(d) + '.key'
csrpath = HOME + "/" + cn + '-' + str(d) + '.csr'
crtpath = HOME + "/" + cn + '-' + str(d) + '.crt'

#Generate the key


def generatekey():

    if os.path.exists(keypath):
        print("Certificate file exists, aborting.")
        print(keypath)
        sys.exit(1)
    #Else write the key to the keyfile
    else:
        print("Generating Key Please standby")
        key.generate_key(TYPE_RSA, 1024)
        f = open(keypath, "w")
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
        f.close()

    #return key

generatekey()

#Generate CSR

def generatecsr():

        cert = crypto.X509()
        cert.get_subject().CN = "hostname"
        cert.get_subject().O = 'hostname.local'
        cert.get_subject().OU = 'hostname'
        cert.get_subject().L = 'local'
        cert.get_subject().ST = 'Spain'
        cert.get_subject().C = 'ES'
        cert.get_subject().emailAddress = 'test@hostname'
        cert.set_serial_number(0)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(20*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(key)
        cert.sign(key, "sha256")

        if os.path.exists(crtpath):
            print "Certificate File Exists, aborting."
            print crtpath
        else:
            f = open(crtpath, "w")
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
            f.close()
            print "CRT Stored Here :" + crtpath

generatecsr()

print "Key Stored Here :" + keypath
print "CSR Stored Here :" + csrpath


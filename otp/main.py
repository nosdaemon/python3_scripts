#!/usr/bin/env python3
# coding: utf-8

import base64, datetime, hashlib, os, sys, unittest
import pyotp


print(pyotp.random_base32())

totp = pyotp.TOTP('base32secret3232')

print(totp.now())

#print(pyotp.hotp.HOTP('JBSWY3DPEHPK3PXP').provisioning_uri("alice@google.com", initial_count=0, issuer_name="Secure App"))

totp = pyotp.TOTP("JBSWY3DPEHPK3PXP")
print("Current OTP:", totp.now())
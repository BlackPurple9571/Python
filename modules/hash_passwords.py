#!/usr/bin/env python
# Description: "A module to create, change and verify hashed passwords."

import base64
import hashlib
import bcrypt  # pip install bcrypt


def create(password: str, salt: bytes = None):
    password = password.encode("utf-8")
    password = base64.b64encode(hashlib.sha512(password).digest())

    if salt is None:
        salt = create_salt()

    hashed = bcrypt.hashpw(
        password,
        salt
    )

    return hashed.decode()


def verify(password: str, hash: str):
    password = password.encode("utf-8")
    password = base64.b64encode(hashlib.sha512(password).digest())
    hash = hash.encode("utf-8")

    if bcrypt.checkpw(password, hash):
        return True
    else:
        return False


def change(old_password: str, new_password: str, hash: str, salt: bytes = None):
    if verify(old_password, hash) is True:
        return create(new_password, salt)
    else:
        return False


def create_salt(rounds: int = 16):
    return bcrypt.gensalt(rounds)

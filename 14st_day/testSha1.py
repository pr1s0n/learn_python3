import hashlib
sha1 = hashlib.sha1()
sha1.update('hello'.encode('utf-8'))
sha1.update('world'.encode('utf-8'))
print(sha1.hexdigest())
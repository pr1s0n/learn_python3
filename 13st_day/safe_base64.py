import base64
def safe_base64_decode(s):
	if len(s) % 4 != 0:
		s = s + b'=' * (4-len(s) % 4)
	return base64.b64decode(s)
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
from jose import jwt
print("Note: this is 4 fun only!!! the secret is literally just 'secret' unless you change the python program")
tknv = input("encode: ")
token = jwt.encode({'key': str(tknv)}, 'secret', algorithm='HS256')
print(token)
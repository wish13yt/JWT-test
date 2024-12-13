from jose import jwt
print("config: secret is secret")
print("algorithm is HS256")
greg = input("load from token.txt or load from input (use input or txt): ")
if (greg == "input" or "Input"):
    token = input("enter JWT token (uses secret as secret): ")
    print(jwt.decode(token, 'secret', algorithms=['HS256']))
if (greg == "txt"):
    f = open("token.txt")
    print(jwt.decode(f.read(), 'secret', algorithms=['HS256']))
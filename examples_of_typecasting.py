

a="200"
print(type(a))

a=int("91")
print(a)

print(int(True))
print(int(False))
print(int(true))
print(int(false))

a=int("krishna66")
print(a)


# converting Float to Integer type
print(int(66.8))

print(int(0b1111))
print(int(0o1111))
print(int(0x10))

#float into other types
print(int(10.4))
print(str(10.50))
print(bool(10.50))

print(0b11.3)#-invalid syntax beacause int cannot convert binary forms
print(0o10.7)
print(0x11.33)

#Boolean into other types
print(int(True))
print(str(True))
print(bool(True))

# INVALID BINARY ITERAL---print(obTrue)
# INVALID BINARY ITERAL---print(ooTrue)
# INVALID BINARY ITERAL---print(oxTrue)

#String into other types
print(int("krishna"))#-invalid literal for int() with base 10: 'krishna'

print(float("krishna"))#could not convert string to float: 'krishna'

print(bool("krishna"))

#String with int into other
print(int("krishna11"))# invalid literal for int() with base 10: 'krishna'
print(str("krishna age is 24"))
print(bool("krishna won 20 rupies"))

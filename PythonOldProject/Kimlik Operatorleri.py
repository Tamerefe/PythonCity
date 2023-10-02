a = 8215763152421536274
b = 8215763152421536274

print(id(a))
print(id(b))
print(id(8))

if a == b:
	print("Esit!")

if a is b:
	print("Kimlik Esit!")
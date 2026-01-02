a=input("Enter the students name :")
try:
 d={'Alice':85,'Tom':55,'John':90,'Sam':95}
 print(a,"'s marks is :",d[a])
except KeyError:
 print("Student not found.")

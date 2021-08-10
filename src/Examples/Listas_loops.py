apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
print(apes[-1])
apes.append("Pan paniscus")
print("There are " + str(len(apes)) + " apes")
monkeys = ["Papio ursinus", "Macaca mulatta"]
print("There are " + str(len(monkeys)) + " monkeys")
print("These are monkeys: ")
apes.extend(monkeys)
print(apes)

s = 'foobar'
print(s[0:3:2])

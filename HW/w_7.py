# Я НЕ ПОНЯЛ ЗНАЧЕНИЕ 
#  difference

fruts = {"яблока", "апельсин", "банан", "апельсин", "виноград", "вишнья", "банан"}
print(set(fruts))

cars = {"mersedes", "BMW", "labarghini"}
Gym = {"Laccety", "Spark", "BMW", "Ferrari"}
z = cars.union(Gym)
print(z)

p = {"apple", "samsung"}
d = {"xiomi", "apple"}
p.update(d)
print(p)

y = ["Jobs", "Hobby", "Stady"]
u = y.pop(1)
print(y)

x = p.copy()
print(x)

g = {"dota1", "Tanks"}
g.add("dota2")
print(g)

i = {"spark", "cobalt", "malibu"}
i.remove("cobalt")
print(i)

o = {"Rossia", "England", "Brazil"}
o.clear()
print(o)

friend = {
    "name": "James",
    "age" : 24,
    "hobby": "Footbal"
}
print(friend.keys(), friend.values(), friend.items(), sep="\n")
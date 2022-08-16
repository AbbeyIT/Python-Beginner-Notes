class Customers:
    greeting = "Welcome to the Coffee Palace!"

c_1 = Customers()
c_1.name = "Samirah"
c_1.beverage = "Iced caffe latte"
c_1.food = "Cinnamon roll"
c_1.total = 225

c_2 = Customers()
c_2.name = "Jerry"
c_2.beverage = "Caramel Macchiato"
c_2.food = "Glazed Doughnut"
c_2.total = 230

print(Customers.greeting)
print(c_1.drink)
print(c_2.food)

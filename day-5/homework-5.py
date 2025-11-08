

1#  
#name = "Lazare Purichamiashvili"

#for ch in name:
    #print(ch)


2#

#for i in name:
    #print(i)


3#

# "for" ციკლი გამოიყენება მაშინ, როცა წინასწარ ვიცით რამდენჯერ გვინდა რომ რაღაც განმეორდეს.

# "while" ციკლი გამოიყენება მაშინ, როცა წინასწარ არ ვიცით რამდენჯერ უნდა განმეორდეს კოდი,
# და გვინდა რომ იმუშავოს მანამ, სანამ გარკვეული პირობა ჭეშმარიტია (True).

4#


#number = 1

#while number <= 10:
    #print(number) 
    #number = number + 1  


5#

#name = input("შეიყვანე შენი სახელი: ")

#vowels = "aeiouAEIOUაეიოუ" 

#count = 0

#for letter in name:
    #if letter in vowels:
        #count = count + 1 


#print("შენ სახელში არის", count, "ხმოვანი ასო.")

#6

password = "lazare123"

guess = input("შეიყვანე პაროლი: ")

while guess != password:
    print("არასწორია! სცადე კიდევ ერთხელ.")
    guess = input("შეიყვანე პაროლი: ")

print("შესანიშნავია! სწორად გამოიცანი პაროლი.")

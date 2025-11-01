# Logical operators — ლოგიკური ოპერატორები
# ისინი გამოიყენება შედარებისას, როცა გვინდა შევამოწმოთ პირობა True ან False მნიშვნელობით


#print(True and True or False or True and True and False)

# ნაბიჯ-ნაბიჯ:
# True and True → True
# True and True and False → False
# ამიტომ შეგვიძლია ჩავანაცვლოთ ასე:
# True or False or False → True

# საბოლოო პასუხი იქნება True


#name = input("Enter your name: ")
#age = int(input("Enter your age: "))

#if name == "John" and age == 25:
    #print(True)
#else:
    #print(False)



#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#num3 = int(input("Enter third number: "))

# საშუალო არითმეტიკული = ჯამი / რაოდენობა
#average = (num1 + num2 + num3) / 3

#print("The average is:", average)




# 1) Sequencing (შეკვეთა)  
# პროგრამაში ბრძანებების შესრულების რიგი. კოდი სრულდება ზუსტად იმ რიგით, როგორც წერია.
x = 2
y = 3
z = x + y
print(z)  # შედეგი: 5
# აქ ზუსტად ამ რიგით ხდება შესრულება: x-ს მნიშვნელობა 2 ეწარმოება, შემდეგ y=3, შემდეგ z = x+y

# 2) Selection (შერჩევა)  
# გამოიყენება, როცა უნდა ავირჩიოთ რომელიმე კოდის ნაწილის შესრულება პირობის მიხედვით (if/else)

#age = 20
#if age >= 18:
    #print("Adult")
#else:
    #print("Minor")

# თუ age 18 ან მეტი → დაბეჭდავს "Adult", წინააღმდეგ შემთხვევაში "Minor"

# 3) Iteration (ციკლი)  
# ერთსა და იმავე კოდის კვანძი რამდენჯერმე უნდა შესრულდეს

#for i in range(5):
    #print(i)

# გამოიტანს: 0,1,2,3,4
# იგივე შეიძლება while ციკლით:

#i = 0
#while i < 5:
    #print(i)
    #i += 1



# For loop გამოიყენება განმეორებადი მოქმედებების შესასრულებლად.

# ყველაზე ხშირად გამოიყენება range() ფუნქციასთან ერთად
# range() შეიძლება მიიღოს 1, 2 ან 3 არგუმენტი

# 1) range(stop)
# ერთი არგუმენტი — ქმნის სერიას 0–დან stop-1-მდე

#for i in range(5):  # 0,1,2,3,4
    #print(i)

# 2) range(start, stop)
# ორი არგუმენტი — ქმნის სერიას start–დან stop-1-მდე

#for i in range(2, 6):  # 2,3,4,5
    #print(i)

# 3) range(start, stop, step)
# სამი არგუმენტი — step განსაზღვრავს რაოდენობას, რამდენ-წამით მიიწევს შემდეგი მნიშვნელობა

#for i in range(1, 10, 2):  # 1,3,5,7,9
    #print(i)



# while loop გამოიყენება, როცა ჩვენ არ ვიცით რამდენჯერ უნდა განმეორდეს კოდი,
# მაგრამ ვიცით პირობა, რომლის მიხედვითაც კოდი უნდა შესრულდეს.

# For loop  0–დან 4-მდე
#for i in range(5):
    #print(i)

# While loop  მანამ, სანამ i < 5
#i = 0
#while i < 5:
    #print(i)
    #i += 1


# მომხმარებლისგან ვიღებთ რიცხვს

#num = int(input("Enter a number: "))

# ფაქტორიალი იწყება 1–დან

#factorial = 1

# for loop-ით ვამრავლებთ ყველა რიცხვს 1–დან num-მდე

#for i in range(1, num + 1):
    #factorial *= i  

#print(f"The factorial of {num} is: {factorial}")



# მომხმარებლისგან ვიღებთ ქულას
#score = int(input("Enter your score: "))

# if-elif-else პირობითი სტრუქტურა ქულის მიხედვით

#if score >= 90:
    #print("A")
#elif score >= 80:
    #print("B")
#elif score >= 70:
    #print("C")
#elif score >= 60:
    #print("D")
#else:
    #print("F")



# მომხმარებლისგან ვიღებთ სამი რიცხვს

#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#c = int(input("Enter third number: "))

# ვამოწმებთ, რომელი რიცხვია უდიდესი

#if a >= b and a >= c:
    #print("The largest number is:", a)
#elif b >= a and b >= c:
    #print("The largest number is:", b)
#else:
    #print("The largest number is:", c)



#for i in range(11): 
    #print(i)



# ცვლადი, სადაც შევინახავთ ჯამს

#total = 0

# for loop 1-დან 20-მდე (ჩათვლით)

#for i in range(1, 21):
    #total += i  

# შედეგის დაბეჭდვა

#rint("The sum of numbers from 1 to 20 is:", total)




# ვქმნით ცვლადს, სადაც შევინახავთ სახელს
name = "Lazare"

# for loop-ის გამოყენებით გადავუვლით თითოეულ სიმბოლოს
for letter in name:
    print(letter)

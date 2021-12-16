# print("Hello World")

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")

# ? Créer et intégrer des variables 
# character_name = "John"
# character_age = 35
# is_male = True

# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old.")

# character_name = "Mike"
# character_age = "20"
# print("He really like the name " + character_name + ", ")
# print("but didn't like being " + character_age + ".")

# ? Type de data 
# * String => "texte"
# * Numbers => 21 ou 21.03
# * Booleans => True or False (les majuscules sont obligatoires)

# ? Travailler avec les Strings
# phrase = "Alexandre Fontaine"
# # print("Alexandre\nFontaine")
# print(phrase.replace("Alexandre", "Julien"))

# * .lower() => met le texte en minuscule
# * .upper() => met le texte en majuscule
# * .islower() => check si le texte est en minuscule
# * .isupper() => check si le texte est en majuscule
# * len() => savoir le nombre de caractères
# * [nombre de l'index voulu] => récupérer le caractère à l'index donné
# * .index() => récupérer l'index grâce au caractère donné
# * .replace("valeur à remplacer", "valeur qui remplace") => remplacer une valeur donné

# ? Travailler avec les chiffres
# from math import *
# ? Sert à faire des imports => imports des fonctions math
# my_num = 5
# print(my_num) 
# * str() => convertir en string => permet de concaténer un chiffre avec une phrase
# * abs() => avoir la valeur absolue d'un chiffre --> -5 = 5 
# * pow() => puissance --> 5^2 = pow(5, 2)
# * max() => retourne la valeur la plus grande entre deux valeurs --> max(4, 6) = 6
# * min() => retourne la valeur la plus petite entre deux valeurs --> min(4, 6) = 4
# * round() => arrondi une valeur décimale --> 3.2 = 3  3.7 = 4 
# * floor() => arrondi une valeur au chiffre inférieur --> 3.2 = 3
# * ceil() => arrondi une valeur au chiffre supérieur --> 3.7 = 4
# * sqrt() => donne la racine carré d'une valeur --> sqrt(36) = 6.0 

# ? Obtenir les inputs des utilisateurs
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age)

# ? Calculatrice basique
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

# ? Texte à trou
# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celrbrity: ")

# print("Roses are " + color)
# print(plural_noun + " are blue ")
# print("I love " + celebrity)

# ? Listes
# friends = [
#     "Kevin", 
#     "Karen", 
#     "Jim", 
#     "Oscar", 
#     "Toby"]
# friends[1] = "Mike"

# print(friends[1:3])
# * Possibilité de référer les index négatifs => donne les index du dernier au premier
# * [n index:] => sert à afficher tout les index à partir de l'index donné n 
# * [n index: n2 index] => sert à afficher les index de n index jusqu'à n2 index non inclus
# * var[n index] = "" => sert à modifier la valeur depuis l'index donné

# ? List Functions
# lucky_numbers = [
#     4,
#     8,
#     15,
#     16,
#     23,
#     42
# ]
# friends = [
#     "Kevin",
#     "Karen",
#     "Jim",
#     "Oscar",
#     "Toby"
# ]
# friends.remove("Jim")

# print(friends)

# * list1.extend(list2) => permet de lier des listes entre elles 
# * list1.append("") => permet d'ajouter une valeur à la fin de la liste 
# * list1.insert(n index, "") => permet d'insérer une valeur dans la liste qui aura pour index n
# * list1.remove("") => permet de retirer une valeur dans la liste 
# * list1.clear() => permet de supprimer toutes les valeurs d'une liste
# * list1.pop() => retire la dernière valeur d'une liste
# * list1.index("") => permet de savoir à quelle index est la valeur donnée
# * list1.count("") => permet de savoir le nombre d'occurence de la valeur donnée
# * list1.sort() => permet de trier par ordre alhabétique les valeurs d'une liste
# * list1.reverse() => affiche les valeurs d'une liste de façon inverse
# * list3 = list1.copy => fait une copie d'une liste existante

# ? Tuples => container où on peut stocker différentes valeurs 
# coordinates = (4, 5)
# print(coordinates[0])

# * Tuples ne sont pas modifiables une fois qu'ils sont instaurés
# * Tuples sont similaires aux listes mais on ne peut pas affecter des valeurs à l'intérieur
# * Tuples sont utilisés quand on sait que les valeurs changeront jamais

# ? Functions
# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age) + ".") 

# say_hi("Alex", 23)
# * def n(): => déclaration de la fonction
# ! L'indentation dans la fonction est importante ! 

# ? Return Statement
# def cube(num):
#     return num*num*num

# result = cube(4)
# print(result)

# ? If Statements
# is_male = True
# is_tall = True

# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but you are tall")
# else:
#     print("You are not a male and not tall")

# * Pour les conditions en "et" => utiliser "and"
# * Pour les conditions en "ou" => utiliser "or"
# * elif => elseif
# * not() => pour demander l'inverse de la conditon initiale

# ? If Statements and Comparisons
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(3, 4, 5))

# ? Meilleure calculatrice
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")

# ? Dictionaries = tableaux associatifs
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
#     }

# print(monthConversions.get("Dec", "Not a valid key")) 

# * L'id est obligatoirement unique 
# * print(dictionarie["n"]) => renvoie la valeur liée à la clé (qui peut être string ou number)
# * print(dictionarie.get("")) => même utilisation que dictionarie["n"], permet de set une valeur par défaut -> print(dictionarie.get("n", "x"))

# ? While loop
# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# print("Done with loop")
# print("i = " + str(i))

# ? Guessing game
# secret_word = "girafe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("Out of guesses, YOU LOSE!")
# else:
#     print("YOU WIN!")

# ? For loop
# friends = ["Jim", "Karen", "Kevin"]
# length = len(friends)

# for index in range(5):
#     if index == 0:
#         print("First itteration")
#     else:
#         print("Not first")
# * La boucle for peut accueillir des strings, des tableaux.., elle est utilisée pour boucler dans une collection 
# * La fonction range(n) permet d'afficher tous les chiffres de 0 à n non-inclus
# * La fonction range(n, n1) permet d'afficher tous les chiffres de n à n1 non-inclus

# ? Exponent function
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(3, 4))
# * print(n**n1) => n^n1 = puissances

# ? 2D Lists and Nested Loops
# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
#     ]

# for row in number_grid:
#     for col in row:
#         print(col)

# ? Build a translator
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiouy":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))

# ?  Try Except
# try:
#     # value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)

# ? Reading files
# employee_file = open("employees.txt", "r") 
# for employee in employee_file.readlines():
#     print(employee)
# employee_file.close()

# * open("fichier à ouvrir", "r" = read => mode de lecture") => permet d'ouvrir un fichier
# * open("fichier à ouvrir", "w" = write => mode de lecture") => permet de réécrire un fichier
# * open("fichier à ouvrir", "a" = append => mode de lecture") => permet modifier un fichier
# * open("fichier à ouvrir", "r+" = read and write => mode de lecture") => permet de lire et d'écrire sur un fichier
# * n_file.close() => permet de fermer un fichier
# * n_file.readable() => permet de savoir si un fichier est lisible ou non
# * n_file.read() => permet d'afficher les informations d'un fichier en lecture
# * n_file.readline() => permet d'afficher une information d'un fichier en lecture
# * n_file.readlines() => permet d'afficher les informations d'un fichier en lecture sous forme d'une liste
# * n_file.readlines()[n1] => permet d'afficher une information d'un fichier en lecture sous forme d'une liste via l'index

# ? Writing to files
# employee_file = open("index.html", "w")
# employee_file.write("<p>This is HTML</p>")
# employee_file.close()

# * n_file.write("\nLoremIpsum") => permet d'ajouter une information à un fichier dans une nouvelle ligne 

# ? Modules and Pip
# import usefull_tools

# print(usefull_tools.roll_dice(10))

# * permet d'importer des fichier Python dans un fichier Python => import des fonctions, variables ...

# * pip pour dl des librairies python => comme composer pour Symfony

# ? Class and objects
# * Travaille avec differentes data
# * cf. student.py
# from student import Student

# student1 = Student('Jim', 'Business', 3.1, False)
# student2 = Student('Pam', 'Art', 2.5, True)
# print(student1.gpa)

# ? Building a multiple choice quiz

# from question import Question


# question_prompts = [
#     'What color are apples?\n(a) Red/Green\n(b) Purple\n (c) Orange\n\n',
#     'What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n',
#     'What color are strawberries?\n(a) Yellow\n(b) Red\n (c) Blue\n\n'
# ]

# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b")
# ]

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print('You got ' + str(score) + '/' + str(len(questions)) + ' correct.')

# run_test(questions)

# ? Object Functions
# from student import Student

# student1 = Student("Oscar", "Accounting", 3.1)
# student2 = Student("Phyllis", "Business", 3.8)

# print(student1.on_honor_roll())
# print(student2.on_honor_roll())

# ? Inheritance

# from chef import Chef
# from chinese_chef import Chinese_chef

# my_chef = Chef()
# my_chef.make_special_dish()
# my_chinese_chef = Chinese_chef()
# my_chinese_chef.make_special_dish()

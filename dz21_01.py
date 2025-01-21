i=0

film= ["Dune: Part Two",
"The Wild Robot",
"Maharaja",
"Spider-Man: Across the Spider-Verse",
"12th Fail",
"Oppenheimer",
"Top Gun: Maverick",
"Spider-Man: No Way Home",
"Jai Bhim",
"Hamilton",
"The Father",
"Parasite",
"Avengers: Endgame"] #список фільмів який я точно не вкрав з вікіпедії

while i == 0:
    do = input("Що ви хочете зробити?\n"
               "Введіть 1 для перегляду списку фільмів\n"
               "Введіть 2 для додавання фільму до списку\n"
               "Введіть 3 для видалення фільму зі списку\n"
               "Введіть 0 для завершення роботи\n")

    if do == "1":
        print("Ось ваш список фільмів:\n", *film)

    elif do == "2":
        add = input("Який фільм ви хочете додати?\n")
        film.append(add)
        print(add, "Додано")

    elif do == "3":
        rem = input("Введіть назву фільму що потрібно видалити\n")
        if rem in film:
            film.remove(rem)
            print(rem, "Видалено")
        else:
            print("Такого фільму в списку немає")

    elif do == "0":
        print("Завершення роботи")
        i = 1

    else:
        print("Такої дії немає")
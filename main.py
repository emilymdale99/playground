def main():
    birth_year = input("In what year were you born? ")
    birth_year = int(birth_year)
    age = 2025-birth_year
    age = str(age)
    print("You are " + age + " years old!")

if __name__ == "__main__":
    main()
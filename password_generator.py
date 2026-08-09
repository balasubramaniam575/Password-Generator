import string
import secrets


def generate_password(length, use_digits=True, use_symbols=True):
    if length < 4:
        return "Password length must be at least 4."

    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def main():
    print("=" * 40)
    print("       PASSWORD GENERATOR")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4.")
            return

        digits = input("Include numbers? (y/n): ").lower() == "y"
        symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(
            length,
            use_digits=digits,
            use_symbols=symbols
        )

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
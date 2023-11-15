def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False

    if s[0].isnumeric() or s[1].isnumeric():
        return False

    first_number = True
    for char in s:
        if char.isnumeric():
            if char == "0" and first_number:
                return False

            first_number = False
        elif not first_number:
            return False

    if s.isalnum():
        return True
    else:
        return False


if __name__ == "__main__":
    main()

while True:
    want_instructions = input("Yes or no? ").lower()

    if want_instructions in ['y', 'yes']:
        print("You chose yes.")
        break

    elif want_instructions in ['n', 'no']:
        print("You chose no.")
        break

    else:
        print("Please choose yes or no.")
        continue

print("we done")

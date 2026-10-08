
shopping_list = []

while True:

    choice = input("add / remove / show / done: ").strip().lower()

    if choice == "add":

        item = input("Item to add: ")

        shopping_list.append(item)

    elif choice == "remove":

        item = input("Item to remove: ")

        if item in shopping_list:

            shopping_list.remove(item)

        else:

            print("That item is not on your list.")

    elif choice == "show":

        for item in shopping_list:

            print(item)

    elif choice == "done":

        print("Goodbye!")

        break

    else:

        print("Invalid choice. Please choose add, remove, show, or done.")


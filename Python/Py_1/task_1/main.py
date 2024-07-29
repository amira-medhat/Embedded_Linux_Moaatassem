import firelink


def print_menu():
    """Prints the menu of favorite websites."""
    print("Please choose a website to open:")
    print("1. Facebook")
    print("2. Google")
    print("3. YouTube")
    print("4. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            firelink.firefox(firelink.facebook_link)
        elif choice == "2":
            firelink.firefox(firelink.google_link)
        elif choice == "3":
            firelink.firefox(firelink.youtube_link)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

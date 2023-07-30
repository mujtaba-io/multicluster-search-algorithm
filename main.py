
# author: mujtaba
# date: july 30, 2023

def main():
    print('Hello to Cluster Search')

    while True:
        print("""
        Press 1 to classify data into clusters
        Press 2 to search within clusters
        Press 3 to exit
        """)

        choice = int(input('Enter your choice: '))
        if choice == 1:
            print('Classifying data into clusters')
        elif choice == 2:
            print('Searching within clusters')
        elif choice == 3:
            print('Exiting')
            break


if __name__ == '__main__':
    main()


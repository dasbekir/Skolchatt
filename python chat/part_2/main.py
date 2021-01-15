from Class import Class
from Group import Group


def main():

    while(True):
        print("1. Manage Classes\n2. Manage Groups\n3. Exit")
        opt = input("\nChoose option: ")
        if opt == "1":
            while(True):
                print(
                    "\n1. Create new Class\n2. Update a Class\n3. Delete Class\n4. Go To main Menu\n")
                opt2 = input("Choose Option: ")
                print("\n")

                if opt2 == "1":
                    name = input("Enter Class Name: ")
                    sTime = input(
                        "Enter class start Timein format(hh/mm AM/PM): ")
                    eTime = input(
                        "Enter class End Timein format(hh/mm AM/PM): ")
                    tName = input("Enter Class Teacher Name: ")
                    loc = input("Enter Class location/Room: ")
                    classs.createNewClass(name, sTime, eTime, tName, loc)

                if opt2 == "2":
                    name = input(
                        "Which Class do you want to update(Enter Class Name): ")
                    classs.updateClassDetails(name)

                if opt2 == "3":
                    name = input(
                        "Which Class do you want to Delete (Enter Class Name): ")
                    classs.deletClass(name)

                if opt2 == "4":
                    break

        elif opt == "2":

            while(True):
                print(
                    "1. Create new Group\n2. Update Group\n3. Delete Group\n4. Go to Main Menu\n\n")
                opt3 = input("Choose Option: ")

                if opt3 == "1":
                    name = input("Enter Group Name: ")
                    students = input(
                        "Enter Number of Students in group: ")
                    performance = input(
                        "Enter Performance Level of group: ")
                    status = input("Enter Status of group: ")
                    group.createNewGroup(name, students, performance, status)

                if opt3 == "2":
                    name = input(
                        "Which Group do you want to update(Enter Group Name): ")
                    group.updateGroupDetails(name)
                if opt3 == "3":
                    name = input(
                        "Which Group do you want to Delete (Enter Group Name): ")
                    group.deletGroup(name)
                if opt3 == "4":
                    break

        elif opt == "3":
            print("\n..... Terminated Successfully...\n")
            # db.closeConnection()
            break


if __name__ == "__main__":

    classs = Class()
    group = Group()
    main()

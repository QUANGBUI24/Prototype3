# MAIN PROGRAM #

from UML_INTERFACE import interface as INTERFACE


def main():
    INTERFACE.main_program_loop()
    # class_string = INTERFACE.get_class_detail("Person")
    # print(class_string)

    # class_details_list = [
    #     INTERFACE.get_class_detail(class_name).split("\n")
    #     for class_name in INTERFACE.UML_MANAGER.class_list
    # ]

    # for ele in class_details_list:
    #     print(ele)

    # for i in range(0, len(class_details_list), 4):
    #     chunk = class_details_list[i : i + 4]
    #     for ele in chunk:
    #         print(ele)


if __name__ == "__main__":
    main()

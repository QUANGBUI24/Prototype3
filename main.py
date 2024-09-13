# MAIN PROGRAM #

# import UML_CORE.UML_CLASS.uml_class as UMLClass

from UML_INTERFACE import interface as INTERFACE


def main():
    INTERFACE.main_program_loop()

    # UMLClass.rename_class("Person", "Human")

    # rel_list = UMLClass.relationship_list
    # for dictionary in rel_list:
    #     print(dictionary)

    # for dictionary in rel_list:
    #     for key, value in dictionary.items():
    #         if value == "Person":
    #             dictionary[key] = "Human"

    # for dictionary in rel_list:
    #     print(dictionary)

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

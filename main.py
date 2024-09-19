# MAIN PROGRAM #

import UML_CORE.UML_CLASS.uml_class as UML_CLASS
import UML_MANAGER.uml_manager as UML_MANAGER
from UML_INTERFACE import interface as INTERFACE


def main():
    # INTERFACE.main_program_loop()

    # file_path = "UML_UTILITY/SAVE_LOAD/SAVED_FILES/test"
    # INTERFACE.UML_MANAGER.data_list = INTERFACE.SAVE_LOAD.load_chosen_saved_file(file_path)
    # temp = INTERFACE.UML_MANAGER.data_list
    # print(type(temp))
    # INTERFACE.display_class_list_detail()

    new_list = INTERFACE.SAVE_LOAD.load_data_from_json("test")
    UML_MANAGER.update_data(new_list)

    INTERFACE.keep_updating_data()

    temp1 = UML_CLASS.data_list
    temp2 = UML_CLASS.class_and_attr_list
    temp3 = UML_CLASS.class_list

    temp_obj = UML_CLASS.get_chosen_class("person")

    print(type(temp3))


if __name__ == "__main__":
    main()

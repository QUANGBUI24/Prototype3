# MAIN PROGRAM #

from UML_INTERFACE import interface as INTERFACE

def main():
    INTERFACE.main_program_loop()
    
    # file_path = "UML_UTILITY/SAVE_LOAD/SAVED_FILES/test"
    # INTERFACE.UML_MANAGER.data_list = INTERFACE.SAVE_LOAD.load_chosen_saved_file(file_path)
    # temp = INTERFACE.UML_MANAGER.data_list
    # print(type(temp))
    # INTERFACE.display_class_list_detail()
    
    
if __name__ == "__main__":
    main()

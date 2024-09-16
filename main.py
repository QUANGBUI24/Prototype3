# MAIN PROGRAM #

# from UML_INTERFACE import interface as INTERFACE
import UML_CORE.UML_CLASS.uml_class as UML_CLASS
import UML_CORE.UML_METHOD.uml_method as METHOD
import UML_UTILITY.SAVE_LOAD.save_load as SAVE_LOAD


def main():
    # INTERFACE.main_program_loop()
    METHOD.add_param("test", "attack", "damage")
    METHOD.add_param("test", "attack", "damage")
    # SAVE_LOAD.save_data_from_json(UML_CLASS.data_list, "data.json")


if __name__ == "__main__":
    main()

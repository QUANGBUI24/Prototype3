################################################################
#   Author : Quang Bui
#   Created: September 12, 2024
#
#   This file has UML class attribute features
################################################################

import UML_CLASS.uml_class as UMLClass

data_list = UMLClass.data_list
class_and_attr_list = UMLClass.class_and_attr_list

################################################################################
# WORKING WITH ATTRIBUTE #

def add_attribute(class_name: str, attribute_name: str):
    class_object = UMLClass.get_chosen_class(class_name)
    

def delete_attribute(class_name: str, attribute_name: str):
    pass

def rename_attribute(class_name: str, attribute_name: str, new_attribute_name: str):
    pass
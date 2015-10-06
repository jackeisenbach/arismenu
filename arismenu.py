#!c:/python26

'''
/*===========================================================================
<arismenu.py>

 Copyright (c) 2015 by QUALCOMM, Incorporated.  All Rights Reserved.
 QUALCOMM Proprietary for MediaFLO

Description:
     This script allows you to enter ARIS commands. 

Revision:
     9/25/2015  <Jack Eisenbach> - initial revision

===========================================================================*/
''' 

import os
import sys 
import cmd
import pickle
from aris_ext_api_mod import ArisExtAPI

from confVars import confVars

ARIS_CLIENT_VERSION = 'V1.0.0'


class aris_menu(cmd.Cmd):
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "\n aris->"
        self.menu()
    
    def menu(self):
        self.cv = confVars()
        self.conf = confVars.getAll(self.cv)
        self.assessment_id = self.conf['assessment_id']
        self.assessment_type = self.conf['assessment_type']
        self.client_root = self.conf['client_root']
        self.client_spec = self.conf['client_spec']
        self.client_spec_file_location = self.conf['client_spec_file_location']
        self.client_spec_file_version = self.conf['client_spec_file_version']
        self.client_spec_p4_server = self.conf['client_spec_p4_server']
        self.client_spec_type = self.conf['client_spec_type']
        self.component_name = self.conf['component_name']
        self.created_by = self.conf['created_by']
        self.crm_build_id = self.conf['crm_build_id']
        self.dependency_list = self.conf['dependency_list']
        self.image_client_id = self.conf['image_client_id']
        self.integration_line_client_id = self.conf['integration_line_client_id']
        self.integration_line_name = self.conf['integration_line_name']
        self.integration_line_level = self.conf['integration_line_level']
        self.is_active = self.conf['is_active']
        self.is_passed = self.conf['is_passed']
        self.is_static_label = self.conf['is_static_label']
        self.iu_client_id = self.conf['iu_client_id']
        self.iu_level = self.conf['iu_level']
        self.iu_name = self.conf['iu_name']
        self.label_level = self.conf['label_level']
        self.label_name = self.conf['label_name']
        self.label_poc = self.conf['label_poc']
        self.label_type = self.conf['label_type']
        self.predecessor = self.conf['predecessor']
        self.state = self.conf['state']
        self.testResultsJson = self.conf['testResultsJson']
        self.user_name = self.conf['user_name']
        self.versioned_iu_name = self.conf['versioned_iu_name']
        self.versioned_iu_level = self.conf['versioned_iu_level']
        
        print "\n     [ARIS Client " + ARIS_CLIENT_VERSION + "]\n\n" + \
        "     ARIS Request Commands\n" + " " + "-"*29 + "\n" + \
        "  1. CreateRequestImageBuildForProduct\n" + \
        "  2. CreateRequestComponentRevisionForImage\n" + \
        "  3. CreateRequestStaticLabelForImage\n" + \
        "  4. CreateRequest\n" + \
        "  5. GetBuildItemsForCrmBuild\n" + \
        "  6. GetDeviceAssessmentsForCrmBuild\n" + \
        "  7. GetIntegrationLineActiveComposition\n" + \
        "  8. GetLabelDetails\n" + \
        "  9. GetLastAssessmentDetail\n" + \
        " 10. GetLastLabels\n" + \
        " 11. RejectResubmittedLabel\n" + \
        " 12. ReSubmitLabel\n" + \
        " 13. RunAssessment\n" + \
        " 14. SaveTestResults\n" + \
        " 15. SaveTestResultsV2\n" + \
        " 16. UpdateRequestState\n" + \
        "  c. Configure function parameters\n\n" + \
        "      (Q)uit ---- Exits\n"

    #--------------------------------------
    #  CreateRequestImageBuildForProducts
    #--------------------------------------
    def do_1(self, line):
        print "CreateRequestImageBuildForProducts using parameters:"
        print "  user_name:", self.user_name
        print "  iu_name:", self.iu_name
        print "  label_name:", self.label_name
        print "  component_name:", self.component_name
        print "  predecessor:", self.predecessor
        print "  iu_client_id:", self.iu_client_id
        print "  image_client_id:", self.image_client_id

        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.create_request_image_build_for_product(
                self.user_name,
                self.iu_name,
                self.label_name,
                self.component_name,
                self.predecessor,
                self.iu_client_id,
                self.image_client_id
               )

        self.menu()

    #--------------------------------------
    #  CreateRequestComponentRevisionForImage
    #--------------------------------------
    def do_2(self, line):
        print "CreateRequestComponentRevisionForImage using parameters:"
        print "  versioned_iu_name:", self.versioned_iu_name
        print "  versioned_iu_level:", self.versioned_iu_level
        print "  iu_name:", self.iu_name
        print "  iu_level:", self.iu_level
        print "  label_name:", self.label_name
        print "  label_type:", self.label_type
        print "  component_name:", self.component_name
        print "  label_level:", self.label_level
        print "  state:", self.state
        print "  label_poc:", self.label_poc
        print "  created_by:", self.created_by
        print "  predecessor:", self.predecessor
        print "  client_root:", self.client_root
        print "  is_active:", self.is_active
        print "  iu_client_id:", self.iu_client_id
        print "  image_client_id:", self.image_client_id
        print "  dependency_list:", self.dependency_list

        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.create_request_component_revision_for_image(
                self.versioned_iu_name,        
                self.versioned_iu_level,       
                self.iu_name,                  
                self.iu_level,                 
                self.label_name,               
                self.label_type,               
                self.component_name,           
                self.label_level,              
                self.state,                    
                self.label_poc,                
                self.created_by,               
                self.predecessor,              
                self.client_root,              
                self.is_active,                
                self.iu_client_id,        
                self.image_client_id,     
                self.dependency_list
                )

        self.menu()

    #--------------------------------------
    #  CreateRequestStaticLabelForImage
    #--------------------------------------
    def do_3(self, line):
        print "CreateRequestStaticLabelForImage using parameters:"
        print "  versioned_iu_name:", self.versioned_iu_name
        print "  versioned_iu_level:", self.versioned_iu_level
        print "  iu_name:", self.iu_name
        print "  iu_level:", self.iu_level
        print "  label_name:", self.label_name
        print "  label_type:", self.label_type
        print "  component_name:", self.component_name
        print "  label_level:", self.label_level
        print "  state:", self.state
        print "  label_poc:", self.label_poc
        print "  created_by:", self.created_by
        print "  predecessor:", self.predecessor
        print "  client_spec:", self.client_spec
        print "  client_spec_type:", self.client_spec_type
        print "  client_spec_p4_server:", self.client_spec_p4_server
        print "  client_spec_file_location:", self.client_spec_file_location
        print "  client_spec_file_version:", self.client_spec_file_version
        print "  client_root:", self.client_root
        print "  is_active:", self.is_active
        print "  is_passed:", self.is_passed
        print "  is_static_label:", self.is_static_label
        print "  iu_client_id:", self.iu_client_id
        print "  image_client_id:", self.image_client_id
        print "  dependency_list:", self.dependency_list

        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.create_request_static_label_for_image(
                self.versioned_iu_name,        
                self.versioned_iu_level,       
                self.iu_name,                  
                self.iu_level,                 
                self.label_name,               
                self.label_type,               
                self.component_name,           
                self.label_level,              
                self.state,                    
                self.label_poc,                
                self.created_by,               
                self.predecessor,              
                self.client_spec,              
                self.client_spec_type,         
                self.client_spec_p4_server,    
                self.client_spec_file_location,
                self.client_spec_file_version, 
                self.client_root,              
                self.is_active,                
                self.is_passed,                
                self.is_static_label,
                self.iu_client_id,        
                self.image_client_id,     
                self.dependency_list
                )

        self.menu()

    #--------------------------------------
    #  CreateRequest
    #--------------------------------------
    def do_4(self, line):
        print "CreateRequest using parameters:"
        print "  versioned_iu_name:", self.versioned_iu_name
        print "  versioned_iu_level:", self.versioned_iu_level
        print "  iu_name:", self.iu_name
        print "  iu_level:", self.iu_level
        print "  label_name:", self.label_name
        print "  label_type:", self.label_type
        print "  component_name:", self.component_name
        print "  label_level:", self.label_level
        print "  state:", self.state
        print "  label_poc:", self.label_poc
        print "  created_by:", self.created_by
        print "  predecessor:", self.predecessor
        print "  client_spec:", self.client_spec
        print "  client_spec_type:", self.client_spec_type
        print "  client_spec_p4_server:", self.client_spec_p4_server
        print "  client_spec_file_location:", self.client_spec_file_location
        print "  client_spec_file_version:", self.client_spec_file_version
        print "  client_root:", self.client_root
        print "  is_active:", self.is_active
        print "  is_passed:", self.is_passed
        print "  is_static_label:", self.is_static_label
        print "  iu_client_id:", self.iu_client_id
        print "  image_client_id:", self.image_client_id
        print "  dependency_list:", self.dependency_list

        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.create_request(
                self.versioned_iu_name,        
                self.versioned_iu_level,       
                self.iu_name,                  
                self.iu_level,                 
                self.label_name,               
                self.label_type,               
                self.component_name,           
                self.label_level,              
                self.state,                    
                self.label_poc,                
                self.created_by,               
                self.predecessor,              
                self.client_spec,              
                self.client_spec_type,         
                self.client_spec_p4_server,    
                self.client_spec_file_location,
                self.client_spec_file_version, 
                self.client_root,              
                self.is_active,                
                self.is_passed,                
                self.is_static_label,
                self.iu_client_id,        
                self.image_client_id,     
                self.dependency_list
                )

        self.menu()

    #--------------------------------------
    #  GetBuildItemsForCrmBuild
    #--------------------------------------
    def do_5(self, line):
        print "GetBuildItemsForCrmBuild using parameters:"
        print "  user_name:", self.user_name 
        print "  crm_build_id:", self.crm_build_id 
        
        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.get_build_items_for_crm_build(self.user_name, 
                                                    self.crm_build_id
                                                   )

        self.menu()

    #--------------------------------------
    #  GetDeviceAssessmentsForCrmBuild
    #--------------------------------------
    def do_6(self, line):
        print "GetDeviceAssessmentsForCrmBuild using parameters:"
        print "  user_name:", self.user_name 
        print "  crm_build_id:", self.crm_build_id 
        
        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.get_device_assessments_for_crm_build(self.user_name, 
                                                           self.crm_build_id
                                                          )

        self.menu()

    #--------------------------------------
    #  GetIntegrationLineActiveComposition
    #--------------------------------------
    def do_7(self, line):
        print "GetIntegrationLineActiveComposition using parameters:"
        print "  user_name:", self.user_name 
        print "  integration_line_name:", self.integration_line_name
        print "  integration_line_level:", self.integration_line_level
        print "  integration_line_client_id:", self.integration_line_client_id
        
        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.get_integration_line_active_composition(self.user_name,
                                                              self.integration_line_name,
                                                              self.integration_line_level,
                                                              self.integration_line_client_id
                                                             )

        self.menu()

    #--------------------------------------
    #  GetLabelDetails
    #--------------------------------------
    def do_8(self, line):
        print "GetLabelDetails using parameters:"
        print "  label_name:", self.label_name

        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.get_label_details(self.label_name)

        self.menu()

    #--------------------------------------
    #  GetLastAssessmentDetail
    #--------------------------------------
    def do_9(self, line):
        print "GetLastAssessmentDetail using parameters:"
        print "  user_name:", self.user_name 
        print "  versioned_iu_name:", self.versioned_iu_name
        print "  versioned_iu_level:", self.versioned_iu_level
        print "  iu_name:", self.iu_name
        print "  iu_level:", self.iu_level
        print "  is_active:", self.is_active
        print "  is_passed:", self.is_passed
        print "  assessment_type:", self.assessment_type
        print "  iu_client_id:", self.iu_client_id

        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.get_last_assessment_detail(self.user_name, 
                                        self.versioned_iu_name, 
                                        self.versioned_iu_level, 
                                        self.iu_name, 
                                        self.iu_level, 
                                        self.is_active, 
                                        self.is_passed, 
                                        self.assessment_type,
                                        self.iu_client_id
                                        )

        self.menu()

    #--------------------------------------
    #  GetLastLabels
    #--------------------------------------
    def do_10(self, line):
        print "GetLastLabels using parameters:"
        print "  user_name:", self.user_name
        print "  state:", self.state
        print "  iu_name:", self.iu_name
        print "  iu_level:", self.iu_level
        print "  iu_client_id:", self.iu_client_id

        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.get_latest_labels(self.user_name, 
                                        self.iu_name, 
                                        self.iu_level, 
                                        self.iu_client_id, 
                                        self.state
                                       )

        self.menu()

    #--------------------------------------
    #  RejectResubmittedLabel
    #--------------------------------------
    def do_11(self, line):
        print "RejectResubmittedLabel using parameters:"
        print "  user_name:", self.user_name 
        
        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.reject_resubmitted_label(self.user_name, 
                                               self.label_name,
                                               self.versioned_iu_name, 
                                               self.versioned_iu_level, 
                                               self.iu_name, 
                                               self.iu_level, 
                                               self.is_active, 
                                               self.iu_client_id
                                              )

        self.menu()

    #--------------------------------------
    #  ReSubmitLabel
    #--------------------------------------
    def do_12(self, line):
        print "ResubmitLabel using parameters:"
        print "  user_name:", self.user_name 
        print "  label_name:", self.label_name 
        print "  versioned_iu_name:", self.versioned_iu_name
        print "  versioned_iu_level:", self.versioned_iu_level
        print "  iu_name:", self.iu_name
        print "  iu_level:", self.iu_level
        print "  is_active:", self.is_active
        print "  iu_client_id:", self.iu_client_id
        
        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.resubmit_label(self.user_name, 
                                     self.label_name,
                                     self.versioned_iu_name, 
                                     self.versioned_iu_level, 
                                     self.iu_name, 
                                     self.iu_level, 
                                     self.is_active, 
                                     self.iu_client_id
                                    )

        self.menu()

    #--------------------------------------
    #  RunAssessment
    #--------------------------------------
    def do_13(self, line):
        print "RunAssessment using parameters:"
        print "  user_name:", self.user_name 
        print "  iu_name:", self.iu_name
        print "  iu_level:", self.iu_level
        print "  iu_client_id:", self.iu_client_id
        
        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.run_assessment(self.user_name, 
                                     self.iu_name, 
                                     self.iu_level, 
                                     self.iu_client_id
                                    )

        self.menu()

    #--------------------------------------
    #  SaveTestResults
    #--------------------------------------
    def do_14(self, line):
        print "SaveTestResults using parameters:"
        print "  user_name:", self.user_name 
        print "  testResultsJson:", self.testResultsJson
        print "  assessment_id:", self.assessment_id
        
        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.save_test_results(self.user_name, 
                                        self.iu_name, 
                                        self.assessment_id
                                       )

        self.menu()

    #--------------------------------------
    #  SaveTestResultsV2
    #--------------------------------------
    def do_15(self, line):
        print "SaveTestResultsV2 using parameters:"
        print "Not complete yet"

        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.save_test_results_v2(self.user_name, 
                                           self.iu_name, 
                                           self.iu_client_id
                                          )

        self.menu()

    #--------------------------------------
    #  UpdateRequestState
    #--------------------------------------
    def do_16(self, line):
        print "UpdateRequestState using parameters:"
        print "  user_name:", self.user_name 
        print "  label_name:", self.label_name
        print "  integration_line_level:", self.integration_line_level
        print "  integration_line_name:", self.integration_line_name
        print "  state:", self.state
        print "  integration_line_client_id:", self.integration_line_client_id
        
        print "\n Press S to Submit or C to Cancel request",
        temp = raw_input()
        if temp == "s":
            self.aris = ArisExtAPI()
            self.aris.update_request_state(self.user_name, 
                                           self.label_name, 
                                           self.integration_line_name,
                                           self.integration_line_level,
                                           self.state,
                                           self.integration_line_client_id
                                          )

        self.menu()


    #--------------------------------------
    #  Config
    #--------------------------------------
    def help_config(self):
        print "Configuration menu to setup various parameters"
    def do_config(self, line):
        conf_menu().cmdloop() 
        self.menu()

    #--------------------------------------
    #  Menu
    #--------------------------------------
    def help_menu(self):
        print "Redraws the menu"
    def do_menu(self, line):
        self.menu()

    #--------------------------------------
    #  Quit ARIS
    #--------------------------------------
    def help_quit(self):
        print "Quits the program"
    def do_quit(self, line):
        sys.exit(1)

    # shortcuts for single letter commands
    help_q = help_quit
    help_e = help_quit
    do_q = do_quit
    do_Q = do_quit
    do_e = do_quit
    do_E = do_quit

    help_c = help_config
    do_c = do_config
    do_C = do_config

    help_m = help_menu
    do_m = do_menu
    do_M = do_menu


class conf_menu(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = " conf->"
        self.config_menu()

    def config_menu(self):
        self.cv = confVars()
        self.conf = confVars.getAll(self.cv)

        self.assessment_id = self.conf['assessment_id']
        self.assessment_type = self.conf['assessment_type']
        self.client_root = self.conf['client_root']
        self.client_spec = self.conf['client_spec']
        self.client_spec_file_location = self.conf['client_spec_file_location']
        self.client_spec_file_version = self.conf['client_spec_file_version']
        self.client_spec_p4_server = self.conf['client_spec_p4_server']
        self.client_spec_type = self.conf['client_spec_type']
        self.component_name = self.conf['component_name']
        self.created_by = self.conf['created_by']
        self.crm_build_id = self.conf['crm_build_id']
        self.dependency_list = self.conf['dependency_list']
        self.image_client_id = self.conf['image_client_id']
        self.integration_line_client_id = self.conf['integration_line_client_id']
        self.integration_line_name = self.conf['integration_line_name']
        self.integration_line_level = self.conf['integration_line_level']
        self.is_active = self.conf['is_active']
        self.is_passed = self.conf['is_passed']
        self.is_static_label = self.conf['is_static_label']
        self.iu_client_id = self.conf['iu_client_id']
        self.iu_level = self.conf['iu_level']
        self.iu_name = self.conf['iu_name']
        self.label_level = self.conf['label_level']
        self.label_name = self.conf['label_name']
        self.label_poc = self.conf['label_poc']
        self.label_type = self.conf['label_type']
        self.predecessor = self.conf['predecessor']
        self.state = self.conf['state']
        self.testResultsJson = self.conf['testResultsJson']
        self.user_name = self.conf['user_name']
        self.versioned_iu_name = self.conf['versioned_iu_name']
        self.versioned_iu_level = self.conf['versioned_iu_level']


        print "\n   ARIS Parameters Configure Menu\n" + \
        " " + "-"*34 + "\n" + \
        "  1. assessment_id:", self.assessment_id + "\n" + \
        "  2. assessment_type:", self.assessment_type + "\n" + \
        "  3. client_root:", self.client_root + "\n" + \
        "  4. client_spec:", self.client_spec + "\n" + \
        "  5. client_spec_file_location:", self.client_spec_file_location + "\n" + \
        "  6. client_spec_file_version:", self.client_spec_file_version + "\n" + \
        "  7. client_spec_p4_server:", self.client_spec_p4_server + "\n" + \
        "  8. client_spec_type:", self.client_spec_type + "\n" + \
        "  9. component_name:", self.component_name + "\n" + \
        " 10. created_by:", self.created_by + "\n" + \
        " 11. crm_build_id:", self.crm_build_id + "\n" + \
        " 12. dependency_list:", self.dependency_list + "\n" + \
        " 13. image_client_id:", self.image_client_id + "\n" + \
        " 14. integration_line_client_id:", self.integration_line_client_id + "\n" + \
        " 15. integration_line_name:", self.integration_line_name + "\n" + \
        " 16. integration_line_level:", self.integration_line_level + "\n" + \
        " 17. is_active:", str(self.is_active) + "\n" + \
        " 18. is_passed:", str(self.is_passed) + "\n" + \
        " 19. is_static_label:", str(self.is_static_label) + "\n" + \
        " 20. iu_client_id:", self.iu_client_id + "\n" + \
        " 21. iu_level:", self.iu_level + "\n" + \
        " 22. iu_name:", self.iu_name + "\n" + \
        " 23. label_level:", self.label_level + "\n" + \
        " 24. label_name:", self.label_name + "\n" + \
        " 25. label_poc:", self.label_poc + "\n" + \
        " 26. label_type:", self.label_type + "\n" + \
        " 27. predecessor:", self.predecessor + "\n" + \
        " 28. state:", self.state + "\n" + \
        " 29. testResultsJson:", self.testResultsJson + "\n" + \
        " 30. user_name:", self.user_name + "\n" + \
        " 31. versioned_iu_name:", self.versioned_iu_name + "\n" + \
        " 32. versioned_iu_level:", self.versioned_iu_level + "\n" + \
        "\n      (Q)uit ---- Exits\n"


    def do_1(self, line):
        print "Enter assessment_id:",
        confVars.set_assessment_id(self.cv, raw_input())
        print "assessment_id:", self.assessment_id
        print "  Enter assessment_id:",

        self.config_menu()

    def do_2(self, line):
        print "Enter assessment_type:",
        confVars.set_assessment_type(self.cv, raw_input())
        print "assessment_type:", self.assessment_type
        print "  Enter assessment_type:",

        self.config_menu()

    def do_3(self, line):
        print "Enter client_root:",
        confVars.set_client_root(self.cv, raw_input())
        print "assessment_type:", self.client_root
        print "  Enter client_root:",

        self.config_menu()

    def do_4(self, line):
        print "Enter client_spec:",
        confVars.set_client_spec(self.cv, raw_input())
        print "client_spec:", self.client_spec
        print "  Enter client_spec:",

        self.config_menu()

    def do_5(self, line):
        print "Enter client_spec_file_location:",
        confVars.set_client_spec_file_location(self.cv, raw_input())
        print "client_spec_file_location:", self.client_spec_file_location
        print "  Enter client_spec_file_location:",

        self.config_menu()

    def do_6(self, line):
        print "Enter client_spec_file_version:",
        confVars.set_client_spec_file_version(self.cv, raw_input())
        print "client_spec_file_version:", self.client_spec_file_version
        print "  Enter client_spec_file_version:",

        self.config_menu()

    def do_7(self, line):
        print "Enter client_spec_p4_server:",
        confVars.set_client_spec_p4_server(self.cv, raw_input())
        print "client_spec_p4_server:", self.client_spec_p4_server
        print "  Enter client_spec_p4_server:",

        self.config_menu()

    def do_8(self, line):
        print "Enter client_spec_type:",
        confVars.set_client_spec_type(self.cv, raw_input())
        print "client_spec_type:", self.client_spec_type
        print "  Enter client_spec_type:",

        self.config_menu()

    def do_9(self, line):
        print "Enter component_name:",
        confVars.set_component_name(self.cv, raw_input())
        print "component_name:", self.component_name
        print "  Enter component_name:",

        self.config_menu()

    def do_10(self, line):
        print "Enter created_by:",
        confVars.set_created_by(self.cv, raw_input())
        print "created_by:", self.created_by
        print "  Enter created_by:",

        self.config_menu()

    def do_11(self, line):
        print "Enter crm_build_id:",
        confVars.set_crm_build_id(self.cv, raw_input())
        print "crm_build_id:", self.crm_build_id
        print "  Enter crm_build_id:",

        self.config_menu()

    def do_12(self, line):
        print "Enter dependency_list:",
        confVars.set_dependency_list(self.cv, raw_input())
        print "dependency_list:", self.dependency_list
        print "  Enter dependency_list:",

        self.config_menu()

    def do_13(self, line):
        print "Enter image_client_id:",
        confVars.set_image_client_id(self.cv, raw_input())
        print "image_client_id:", self.image_client_id
        print "  Enter image_client_id:",

        self.config_menu()

    def do_14(self, line):
        print "Enter integration_line_client_id:",
        confVars.set_integration_line_client_id(self.cv, raw_input())
        print "integration_line_client_id:", self.integration_line_client_id
        print "  Enter integration_line_client_id:",

        self.config_menu()

    def do_15(self, line):
        print "Enter integration_line_name:",
        confVars.set_integration_line_name(self.cv, raw_input())
        print "integration_line_name:", self.integration_line_name
        print "  Enter integration_line_name:",

        self.config_menu()

    def do_16(self, line):
        self.ill = confVars.get_integration_line_level(self.cv)
        if self.ill == "SoftwareProduct":
            confVars.set_integration_line_level(self.cv, "SoftwareImage")
        else:
            confVars.set_integration_line_level(self.cv, "SoftwareProduct")
        self.config_menu()

    def do_17(self, line):
        self.isa = confVars.get_is_active(self.cv)
        if self.isa == 1:
            confVars.set_is_active(self.cv, 0)
        else:    
            confVars.set_is_active(self.cv, 1)
        self.config_menu()

    def do_18(self, line):
        self.isp = confVars.get_is_passed(self.cv)
        if self.isp == 1:
            confVars.set_is_passed(self.cv, 0)
        else:    
            confVars.set_is_passed(self.cv, 1)
        self.config_menu()

    def do_19(self, line):
        self.isl = confVars.get_is_static_label(self.cv)
        if self.isl == 1:
            confVars.set_is_static_label(self.cv, 0)
        else:    
            confVars.set_is_static_label(self.cv, 1)
        self.config_menu()

    def do_20(self, line):
        print "Enter iu_client_id:",
        confVars.set_iu_client_id(self.cv, raw_input())
        print "iu_client_id:", self.iu_client_id
        print "  Enter iu_client_id:",

        self.config_menu()

    def do_21(self, line):
        self.il = confVars.get_iu_level(self.cv)
        if self.il == "Product":
            confVars.set_iu_level(self.cv, "ProductLine")
        elif self.il == "ProductLine":
            confVars.set_iu_level(self.cv, "Area")
        elif self.il == "Area":
            confVars.set_iu_level(self.cv, "Subsystem")
        elif self.il == "Subsystem":
            confVars.set_iu_level(self.cv, "Unit")
        elif self.il == "Unit":
            confVars.set_iu_level(self.cv, "Software Product")
        elif self.il == "Software Product":
            confVars.set_iu_level(self.cv, "Software Image")
        else:
            confVars.set_iu_level(self.cv, "Product")
        self.config_menu()

    def do_22(self, line):
        print "Enter iu_name:",
        confVars.set_iu_name(self.cv, raw_input())
        print "iu_name:", self.iu_name
        print "  Enter iu_name:",

        self.config_menu()

    def do_23(self, line):
        self.lal = confVars.get_label_level(self.cv)
        if self.lal == "ProductLine":
            confVars.set_label_level(self.cv, "Area") 
        elif self.lal == "Area":
            confVars.set_label_level(self.cv, "Subsystem") 
        elif self.lal == "Subsystem":
            confVars.set_label_level(self.cv, "Unit") 
        elif self.lal == "Unit":
            confVars.set_label_level(self.cv, "Component") 
        else: 
            confVars.set_label_level(self.cv, "ProductLine") 

        self.config_menu()

    def do_24(self, line):
        print "Enter label_name:",
        confVars.set_label_name(self.cv, raw_input())
        print "label_name:", self.label_name
        print "  Enter label_name:",

        self.config_menu()

    def do_25(self, line):
        print "Enter label_poc:",
        confVars.set_label_poc(self.cv, raw_input())
        print "label_poc:", self.label_poc
        print "  Enter label_poc:",

        self.config_menu()

    def do_26(self, line):
        self.lt = confVars.get_label_type(self.cv)
        if self.lt == "DirectAsset":
            confVars.set_label_type(self.cv, "PLFLabel")
        elif self.lt == "PLFLabel":
            confVars.set_label_type(self.cv, "CRMBuildId")
        else:
            confVars.set_label_type(self.cv, "DirectAsset")
        self.config_menu()

    def do_27(self, line):
        print "Enter predecessor:",
        confVars.set_predecessor(self.cv, raw_input())
        print "predecessor:", self.predecessor
        print "  Enter predecessor:",

        self.config_menu()

    def do_28(self, line):
        self.state = confVars.get_state(self.cv)
        if self.state == "Defined":
            confVars.set_state(self.cv, "Submitted") 
        elif self.state == "Submitted":
            confVars.set_state(self.cv, "InIntegration") 
        elif self.state == "InIntegration":
            confVars.set_state(self.cv, "Integrated") 
        elif self.state == "Integrated":
            confVars.set_state(self.cv, "Rejected") 
        elif self.state == "Rejected":
            confVars.set_state(self.cv, "ReSubmitted") 
        elif self.state == "ReSubmitted":
            confVars.set_state(self.cv, "InTest") 
        elif self.state == "InTest":
            confVars.set_state(self.cv, "Tested") 
        elif self.state == "Tested":
            confVars.set_state(self.cv, "CIIntegrated") 
        elif self.state == "CIIntegrated":
            confVars.set_state(self.cv, "All") 
        else:
            confVars.set_state(self.cv, "Defined") 
        self.config_menu()

    def do_29(self, line):
        print "Enter testResultsJson:",
        confVars.set_testResultsJson(self.cv, raw_input())
        print "testResultsJson:", self.testResultsJson
        print "  Enter testResultsJson:",

        self.config_menu()

    def do_30(self, line):
        print "Enter user_name:",
        confVars.set_user_name(self.cv, raw_input())
        print "user_name:", self.user_name
        print "  Enter user_name:",

        self.config_menu()

    def do_31(self, line):
        print "Enter versioned_iu_name:",
        confVars.set_versioned_iu_name(self.cv, raw_input())
        print "versioned_iu_name:", self.versioned_iu_name
        print "  Enter versioned_iu_name:",

        self.config_menu()

    def do_32(self, line):
        self.vil = confVars.get_versioned_iu_level(self.cv)
        if self.vil == "Product":
            confVars.set_versioned_iu_level(self.cv, "ProductLine")
        elif self.vil == "ProductLine":
            confVars.set_versioned_iu_level(self.cv, "Area")
        elif self.vil == "Area":
            confVars.set_versioned_iu_level(self.cv, "Subsystem")
        elif self.vil == "Subsystem":
            confVars.set_versioned_iu_level(self.cv, "Unit")
        else:
            confVars.set_versioned_iu_level(self.cv, "Product")
        self.config_menu()


    #--------------------------------------
    #  Quit Config
    #--------------------------------------
    def help_quit(self):
        print "Quits config"
    def do_quit(self, line):
        return True


    # shortcuts for single letter commands
    
    help_q = help_quit
    help_e = help_quit
    do_q = do_quit
    do_e = do_quit



if __name__ == '__main__':
    aris_menu().cmdloop(' Enter a command:') 


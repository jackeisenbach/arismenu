#!/usr/bin/python

'''
/*===========================================================================
<confVars.py>

 Copyright (c) 2015 by QUALCOMM, Incorporated.  All Rights Reserved.

Description:
     This file handles configuration variables for the aris client. 

Revision:
     9/25/15   <Jack Eisenbach> - initial revision

===========================================================================*/
''' 
import pickle
import sys

global cfgFilename
cfgFilename = "conf.pkl"

class confVars():
    """
    Retrieves the config variables from the file
    config file. (Pickle file)
    """
        
    def setCfgFilename(self, configFilename):
        global cfgFilename
        if configFilename == None:
            cfgFilename = "conf.pkl"
        else:
            cfgFilename = configFilename
            
    def loadVars(self):
        global cfgFilename
        try:
            fin = open(cfgFilename, 'rb')
        except IOError:
            # If the config file did not exist, create it and 
            # initialize the config vars to the default settings.
            conf = {
                    'assessment_id': '1',
                    'assessment_type': 'Build',
                    'client_root': '',
                    'client_spec': '',
                    'client_spec_file_location': '',
                    'client_spec_file_version': '1',
                    'client_spec_p4_server': 'qctp401:1666',
                    'client_spec_type': '["File"]',
                    'component_name': 'QSWAT.TESTA.1.0',
                    'created_by': 'c_jacke',
                    'crm_build_id': 'MPSS.TA.2.0.r4-00001-8976_GEN_TEST-1',
                    'dependency_list': '',
                    'image_client_id': 'STD.INT',
                    'integration_line_client_id': 'STD.INT',
                    'integration_line_name': 'QSWAT.TESTA.1.0-00000-STD.INT-4',
                    'integration_line_level': 'Software Image',
                    'is_active': 1,
                    'is_passed': 1,
                    'is_static_label': 0,
                    'iu_client_id': 'STD.INT',
                    'iu_level': 'Product',
                    'iu_name': 'MSM8996.LA.1.0',
                    'label_level': 'Product',
                    'label_name': 'build.tz.1.0-00061',
                    'label_poc': 'c_jacke',
                    'label_type': 'CRMBuildId',
                    'predecessor': 'QSWAT.TESTA.1.0-00000-STD.INT-4',
                    'state': 'Submitted',
                    'testResultsJson': '',
                    'user_name': 'c_jacke',
                    'versioned_iu_level': 'Product',
                    'versioned_iu_name': 'MSM8996.LA.1.0'
                   }

            selfref_list = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
            selfref_list.append(selfref_list)
            fout = open(cfgFilename, 'wb')
            pickle.dump(conf, fout)
            pickle.dump(selfref_list, fout, -1)
            fout.close()
            fin = open(cfgFilename, 'rb')

        finally:                   
            self.conf = pickle.load(fin)
            fin.close()
            
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
            

    def getAll(self):
        self.loadVars()
        return self.conf

    def getVar(self, varName):
        self.loadVars()
        return self.conf[varName]
    
    def setVar(self, varName):
        self.loadVars()
        self.varName = varName
        self.saveVars()


    def get_assessment_id(self):
        self.loadVars()
        return self.conf['assessment_id']

    def set_assessment_id(self, assessment_id):
        self.loadVars()
        self.assessment_id = assessment_id
        self.saveVars()

    def get_assessment_type(self):
        self.loadVars()
        return self.conf['assessment_type']

    def set_assessment_type(self, assessment_type):
        self.loadVars()
        self.assessment_type = assessment_type
        self.saveVars()

    def get_client_root(self):
        self.loadVars()
        return self.conf['client_root']

    def set_client_root(self, client_root):
        self.loadVars()
        self.client_root = client_root
        self.saveVars()

    def get_client_spec(self):
        self.loadVars()
        return self.conf['client_spec']

    def set_client_spec(self, client_spec):
        self.loadVars()
        self.client_spec = client_spec
        self.saveVars()

    def get_client_spec_file_location(self):
        self.loadVars()
        return self.conf['client_spec_file_location']

    def set_client_spec_file_location(self, client_spec_file_location):
        self.loadVars()
        self.client_spec_file_location = client_spec_file_location
        self.saveVars()

    def get_client_spec_file_version(self):
        self.loadVars()
        return self.conf['client_spec_file_version']

    def set_client_spec_file_version(self, client_spec_file_version):
        self.loadVars()
        self.client_spec_file_version = client_spec_file_version
        self.saveVars()

    def get_client_spec_p4_server(self):
        self.loadVars()
        return self.conf['client_spec_p4_server']

    def set_client_spec_p4_server(self, client_spec_p4_server):
        self.loadVars()
        self.client_spec_p4_server = client_spec_p4_server
        self.saveVars()

    def get_client_spec_type(self):
        self.loadVars()
        return self.conf['client_spec_type']

    def set_client_spec_type(self, client_spec_type):
        self.loadVars()
        self.client_spec_type = client_spec_type
        self.saveVars()

    def get_component_name(self):
        self.loadVars()
        return self.conf['component_name']

    def set_component_name(self, component_name):
        self.loadVars()
        self.component_name = component_name
        self.saveVars()

    def get_created_by(self):
        self.loadVars()
        return self.conf['created_by']

    def set_created_by(self, created_by):
        self.loadVars()
        self.created_by = created_by
        self.saveVars()

    def get_crm_build_id(self):
        self.loadVars()
        return self.conf['crm_build_id']

    def set_crm_build_id(self, crm_build_id):
        self.loadVars()
        self.crm_build_id = crm_build_id
        self.saveVars()

    def get_dependency_list(self):
        self.loadVars()
        return self.conf['dependency_list']

    def set_dependency_list(self, dependency_list):
        self.loadVars()
        self.dependency_list = dependency_list
        self.saveVars()

    def get_image_client_id(self):
        self.loadVars()
        return self.conf['image_client_id']

    def set_image_client_id(self, image_client_id):
        self.loadVars()
        self.image_client_id = image_client_id
        self.saveVars()

    def get_integration_line_client_id(self):
        self.loadVars()
        return self.conf['integration_line_client_id']

    def set_integration_line_client_id(self, integration_line_client_id):
        self.loadVars()
        self.integration_line_client_id = integration_line_client_id
        self.saveVars()

    def get_integration_line_name(self):
        self.loadVars()
        return self.conf['integration_line_name']

    def set_integration_line_name(self, integration_line_name):
        self.loadVars()
        self.integration_line_name = integration_line_name
        self.saveVars()

    def get_integration_line_level(self):
        self.loadVars()
        return self.conf['integration_line_level']

    def set_integration_line_level(self, integration_line_level):
        self.loadVars()
        self.integration_line_level = integration_line_level
        self.saveVars()

    def get_is_active(self):
        self.loadVars()
        return self.conf['is_active']

    def set_is_active(self, is_active):
        self.loadVars()
        self.is_active = is_active
        self.saveVars()

    def get_is_passed(self):
        self.loadVars()
        return self.conf['is_passed']

    def set_is_passed(self, is_passed):
        self.loadVars()
        self.is_passed = is_passed
        self.saveVars()

    def get_is_static_label(self):
        self.loadVars()
        return self.conf['is_static_label']

    def set_is_static_label(self, is_static_label):
        self.loadVars()
        self.is_static_label = is_static_label
        self.saveVars()

    def get_iu_client_id(self):
        self.loadVars()
        return self.conf['iu_client_id']

    def set_iu_client_id(self, iu_client_id):
        self.loadVars()
        self.iu_client_id = iu_client_id
        self.saveVars()

    def get_iu_level(self):
        self.loadVars()
        return self.conf['iu_level']

    def set_iu_level(self, iu_level):
        self.loadVars()
        self.iu_level = iu_level
        self.saveVars()

    def get_iu_name(self):
        self.loadVars()
        return self.conf['iu_name']

    def set_iu_name(self, iu_name):
        self.loadVars()
        self.iu_name = iu_name
        self.saveVars()

    def get_label_level(self):
        self.loadVars()
        return self.conf['label_level']

    def set_label_level(self, label_level):
        self.loadVars()
        self.label_level = label_level
        self.saveVars()

    def get_label_name(self):
        self.loadVars()
        return self.conf['label_name']

    def set_label_name(self, label_name):
        self.loadVars()
        self.label_name = label_name
        self.saveVars()

    def get_label_poc(self):
        self.loadVars()
        return self.conf['label_poc']

    def set_label_poc(self, label_poc):
        self.loadVars()
        self.label_poc = label_poc
        self.saveVars()

    def get_label_type(self):
        self.loadVars()
        return self.conf['label_type']

    def set_label_type(self, label_type):
        self.loadVars()
        self.label_type = label_type
        self.saveVars()

    def get_predecessor(self):
        self.loadVars()
        return self.conf['predecessor']

    def set_predecessor(self, predecessor):
        self.loadVars()
        self.predecessor = predecessor
        self.saveVars()

    def get_state(self):
        self.loadVars()
        return self.conf['state']

    def set_state(self, state):
        self.loadVars()
        self.state = state
        self.saveVars()

    def get_testResultsJson(self):
        self.loadVars()
        return self.conf['testResultsJson']

    def set_testResultsJson(self, testResultsJson):
        self.loadVars()
        self.testResultsJson = testResultsJson
        self.saveVars()

    def get_user_name(self):
        self.loadVars()
        return self.conf['user_name']

    def set_user_name(self, user_name):
        self.loadVars()
        self.user_name = user_name
        self.saveVars()

    def get_versioned_iu_name(self):
        self.loadVars()
        return self.conf['versioned_iu_name']

    def set_versioned_iu_name(self, versioned_iu_name):
        self.loadVars()
        self.versioned_iu_name = versioned_iu_name
        self.saveVars()

    def get_versioned_iu_level(self):
        self.loadVars()
        return self.conf['versioned_iu_level']

    def set_versioned_iu_level(self, versioned_iu_level):
        self.loadVars()
        self.versioned_iu_level = versioned_iu_level
        self.saveVars()

    def saveVars(self):
        conf = {
                'assessment_id': self.assessment_id,
                'assessment_type': self.assessment_type,
                'client_root': self.client_root,
                'client_spec': self.client_spec,
                'client_spec_file_location': self.client_spec_file_location, 
                'client_spec_file_version': self.client_spec_file_version,
                'client_spec_p4_server': self.client_spec_p4_server,
                'client_spec_type': self.client_spec_type,
                'component_name': self.component_name,
                'created_by': self.created_by,
                'crm_build_id': self.crm_build_id,
                'dependency_list': self.dependency_list,
                'image_client_id': self.image_client_id,
                'integration_line_client_id': self.integration_line_client_id,
                'integration_line_name': self.integration_line_name,
                'integration_line_level': self.integration_line_level,
                'is_active': self.is_active,
                'is_passed': self.is_passed,
                'is_static_label': self.is_static_label,
                'iu_client_id': self.iu_client_id,
                'iu_level': self.iu_level,
                'iu_name': self.iu_name,
                'label_level': self.label_level,
                'label_name': self.label_name,
                'label_poc': self.label_poc,
                'label_type': self.label_type,
                'predecessor': self.predecessor,
                'state': self.state,
                'testResultsJson': self.testResultsJson,
                'user_name': self.user_name,
                'versioned_iu_name': self.versioned_iu_name,
                'versioned_iu_level': self.versioned_iu_level
               }
                
        selfref_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
        selfref_list.append(selfref_list)
        fout = open(cfgFilename, 'wb')
        pickle.dump(conf, fout)
        pickle.dump(selfref_list, fout, -1)
        fout.close()

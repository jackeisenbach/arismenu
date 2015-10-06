#===============================================================================
#
# Copyright (c) 2015 Qualcomm Technologies, Inc. All Rights Reserved.
# Qualcomm Technologies Proprietary and Confidential.
#
#===============================================================================
'''
    Created on Sept. 3, 2015
    @authors: c_jacke, cvempral

    The Asset Readiness & Integration System (ARIS) is a web-based application 
    for labeling and submitting software that is ready for integration. ARIS 
    also tracks the status of your integration requests and software builds.
'''

import suds
import json
import logging
from suds.client import Client
#from sectools.common.utils.c_logging import logger
#from sectools.common.utils.tool_intfs import Tools as ToolBase


""" Todo - Check input parameters for correct type, values, etc.
           Add the following:
                RejectResubmittedLabel
                GetIntegrationLineActiveComposition
                SaveTestResultsV2

           Test the following:
                CreateRequest
                ReSubmitLabel
                RejectResubmittedLabel
                GetIntegrationLineActiveComposition
                UpdateRequstState
                SaveTestResults
                SaveTestResultsV2
"""


"""
The following ARIS External API commands (12) can be used with this lib:
------------------------------------------------------------------------
CreateRequest
GetBuildItemsForCrmBuild
GetDeviceAssessmentsForCrmBuild
GetIntegrationLineActiveComposition
GetLabelDetails
GetLastAssessmentDetail
GetLastLabels
RejectResubmittedLabel
ReSubmitLabel
RunAssessment
SaveTestResults
SaveTestResultsV2
UpdateRequestState

Documentation below was created from:
    
    client = Client(url)
    print "Client:", client


Client:
Suds ( https://fedorahosted.org/suds/ )  version: 0.4 GA  build: R699-20100913

Service ( ArisExternalService ) tns="http://arisservice.qualcomm.com/ArisExternalService"
   Prefixes (9)
      ns0 = "http://arisservice.qualcomm.com/ArisExternalService"
      ns1 = "http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities"
      ns2 = "http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Entities"
      ns3 = "http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations"
      ns4 = "http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts"
      ns5 = "http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests"
      ns6 = "http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Responses"
      ns7 = "http://schemas.microsoft.com/2003/10/Serialization/"
      ns8 = "http://schemas.microsoft.com/2003/10/Serialization/Arrays"
   Ports (1):
      (BasicHttpEndPoint)
         Methods (13):
            CreateRequest(ns5:RequestDetailRequest request, )
            GetBuildItemsForCrmBuild(ns5:GetBuildItemsForCrmBuildRequest request, )
            GetDeviceAssessmentsForCrmBuild(ns5:GetDeviceAssessmentsForCrmBuildRequest request, )
            GetIntegrationLineActiveComposition(ns5:GetIntegrationLineActiveCompositionRequest request, )
            GetLabelDetails(ns5:LabelDetailRequest request, )
            GetLastAssessmentDetail(ns5:AssessmentDetailRequest request, )
            GetLastLabels(ns5:GetLatestLabelsRequest request, )
            ReSubmitLabel(ns5:ReSubmitLabelRequest request, )
            RejectResubmittedLabel(ns5:RejectResubmittedLabelRequest request, )
            RunAssessment(ns5:RunAssessmentRequest request, )
            SaveTestResults(ns5:SaveTestResultsRequest request, )
            SaveTestResultsV2(ns5:SaveTestResultsV2Request request, )
            UpdateRequestState(ns5:UpdateRequestStateRequest request, )
         Types (81):
            ns4:AmTestResultDetail
            ns4:AmTestResultDetailV2
            ns4:ArrayOfAmTestResultDetail
            ns4:ArrayOfAmTestResultDetailV2
            ns4:ArrayOfCcTestResultDetail
            ns4:ArrayOfCcTestResultDetailV2
            ns1:ArrayOfComponentLabelInfo
            ns1:ArrayOfComponentRevisionInfo
            ns4:ArrayOfCompositionItemView
            ns4:ArrayOfDeviceAssessmentDetail
            ns4:ArrayOfEcTestResultDetail
            ns4:ArrayOfEcTestResultDetailV2
            ns4:ArrayOfIntegrationUnitItemInfo
            ns1:ArrayOfLabelInfo
            ns6:ArrayOfParticipatedLabel
            ns4:ArrayOfRequestLabelSummary
            ns4:ArrayOfRequestSummary
            ns4:ArrayOfSourceClientMappingView
            ns8:ArrayOfstring
            ns5:AssessmentDetailRequest
            ns6:AssessmentDetailResponse
            ns4:AssessmentType
            ns5:BaseRequest
            ns6:BaseResponse
            ns1:BuildItemInfo
            ns6:BuildItemsResponse
            ns4:CcTestResultDetail
            ns4:CcTestResultDetailV2
            ns4:CodeBase
            ns4:CodeBaseType
            ns1:ComponentLabelInfo
            ns1:ComponentRevisionInfo
            ns4:CompositionItemView
            ns4:DeviceAssessmentDetail
            ns4:EcTestResultDetail
            ns4:EcTestResultDetailV2
            ns5:GetBuildItemsForCrmBuildRequest
            ns5:GetDeviceAssessmentsForCrmBuildRequest
            ns6:GetDeviceAssessmentsForCrmBuildResponse
            ns5:GetIntegrationLineActiveCompositionRequest
            ns6:GetIntegrationLineActiveCompositionResponse
            ns5:GetLatestLabelsRequest
            ns6:GetLatestLabelsResponse
            ns5:IntegrationLineBaseRequest
            ns3:IntegrationLineItemLevel
            ns3:IntegrationType
            ns5:IntegrationUnitBaseRequest
            ns4:IntegrationUnitItemInfo
            ns4:IntegrationUnitSummary
            ns5:IuBaseRequest
            ns5:LabelDetailRequest
            ns6:LabelDetailsResponse
            ns1:LabelInfo
            ns4:LabelLevel
            ns5:LabelRequest
            ns3:LabelState
            ns4:LabelSummary
            ns4:LabelType
            ns6:ParticipatedLabel
            ns4:PhNodeLevel
            ns5:ReSubmitLabelRequest
            ns6:ReSubmitLabelResponse
            ns5:RejectResubmittedLabelRequest
            ns6:RejectResubmittedLabelResponse
            ns5:RequestDetailRequest
            ns4:RequestLabelSummary
            ns4:RequestSummary
            ns5:RunAssessmentRequest
            ns2:RunWorkflowResult
            ns5:SaveTestResultsRequest
            ns5:SaveTestResultsV2Request
            ns4:SourceClientMappingView
            ns6:SuccessResponse
            ns4:TestResultDetail
            ns4:TestResultDetailV2
            ns3:TestResultStatus
            ns5:UpdateRequestStateRequest
            ns3:VcsServerType
            ns7:char
            ns7:duration
            ns7:guid


phNodeLevel: (ns4:PhNodeLevel){
   Product = "Product"
   ProductLine = "ProductLine"
   Area = "Area"
   Subsystem = "Subsystem"
   Unit = "Unit"
   Component = "Component"
 }

labelType: (ns4:LabelType){
   Unknown = "Unknown"
   DirectAsset = "DirectAsset"
   PLFLabel = "PLFLabel"
   CRMBuildId = "CRMBuildId"
 }

labelLevel: (ns4:LabelLevel){
   Unknown = "Unknown"
   Product = "Product"
   ProductLine = "ProductLine"
   Area = "Area"
   Subsystem = "Subsystem"
   Unit = "Unit"
   Component = "Component"
 }

clientSpec: (CodeBase){
   ClientSpecFileLocation = None
   ClientSpecFileVersion = None
   ClientSpecP4Server = None
   ClientSpecType =
      (CodeBaseType){
         value = None
      }
 }

codeBaseType: (ns4:CodeBaseType){
   Unknown = "Unknown"
   Baseline = "Baseline"
   File = "File"
 }

dependencyList: (ArrayOfstring){
   string[] = <empty>
 }

"""


# Staging server
STAGING_ARIS_URL = 'http://cbistaging.qualcomm.com/ArisService/ArisExternalService.svc?Wsdl'

# Production server
PRODUCTION_ARIS_URL = 'http://hci/ArisService/ArisExternalService.svc?Wsdl'

client = Client(PRODUCTION_ARIS_URL)
#client = Client(STAGING_ARIS_URL)

#logging.basicConfig(filename='aris.log',level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)


class ArisExtAPI():

    def __init__(self):
        self.__name__ = 'ARIS_Ext_API'
#        logging.info("Client:" + str(client))
        logging.debug("Client:" + str(client))

    def create_request_image_build_for_product(self,
                      user_name,                 # Multiple users are ok (comma separated)
                      iu_name,                   # Image name or the Product name
                      label_name,                # Case sensitive string
                      component_name,            # Productline/area/subsystem/unit
                      predecessor,               # Case sensitive string
                      iu_client_id=None,         # Name of the product variant when IuLevel is Product and LabelType is CRMBuildId
                      image_client_id=None):     # Variant. Required when LabelType is CRMBuildId and LabelLevel is ProductLine

        """Create Request allows a user to create a single request with 
           either an existing or non-existing label. This method only supports 
           setting states with 'Defined' or 'Submitted'.
           
           Using create requests you can submit crm builds, component revisions 
           and perforce labels to Aris. For example if you have a component 
           revision on component c1 which belongs to software image I1, you can 
           create a request to submit the component revision on C1 to image I1. 
           This way the next aris assessment will pick up that component revision 
           and make an image build with that revision along with other submitted 
           revisions on other components under the image.
        """
        try:
            # Creating Request Detail
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}RequestDetailRequest')
            labelState = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}LabelState')
            
            request.LabelName = label_name
            request.ComponentName = component_name
            request.IuName = iu_name
            request.VersionedIuName = iu_name
            request.LabelPoc = user_name
            request.CreatedBy = user_name
            request.Predecessor = predecessor
            request.ClientRoot = ""
            request.State = labelState["Submitted"]
            request.IsActive = 1
            request.IuClientId = iu_client_id
            request.ImageClientId = image_client_id
        
            # Assign PhNodeLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            phNodeLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}PhNodeLevel')
            request.IuLevel = phNodeLevel["Product"]
            request.VersionedIuLevel = phNodeLevel["Product"]
            
            # Assign LabelType Enum Value -> DirectAsset, PLFLabel,  CRMBuildId
            labelType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}LabelType')
            request.LabelType = labelType["CRMBuildId"]
            
            # Assign LabelLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            labelLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}LabelLevel')
            request.LabelLevel = labelLevel["ProductLine"]

            # Send Request
            logging.info("\nRequest:" + str(request))
            response = client.service.CreateRequest(request)
            logging.info("Response:" + str(response))
            return response

        except Exception as ex:
            logging.info("Exception:" + str(ex))


    def create_request_component_revision_for_image(self,
                      versioned_iu_name,         # Image name or the Product name
                      versioned_iu_level,        # Product or Product line
                      iu_name,                   # Image name or the Product name
                      iu_level,                  # Product or Product line
                      label_name,                # Case sensitive string
                      label_type,                # Direct asset, PLFLabel, CRMBuildId
                      component_name,            # Productline/area/subsystem/unit
                      label_level,               # Product line, Area, Subsystem, Unit, Component
                      state,                     # Defined or Submitted
                      label_poc,                 # Multiple users are ok (comma separated)
                      created_by,                #
                      predecessor,               # Case sensitive string
                      client_root,               # client_root
                      is_active,                 #
                      iu_client_id=None,         # Name of the product variant when IuLevel is Product and LabelType is CRMBuildId
                      image_client_id=None,      # Variant. Required when LabelType is CRMBuildId and LabelLevel is ProductLine
                      dependency_list=None):     #

        """Create Request allows a user to create a single request with 
           either an existing or non-existing label. This method only supports 
           setting states with 'Defined' or 'Submitted'.
           
           Using create requests you can submit crm builds, component revisions 
           and perforce labels to Aris. For example if you have a component 
           revision on component c1 which belongs to software image I1, you can 
           create a request to submit the component revision on C1 to image I1. 
           This way the next aris assessment will pick up that component revision 
           and make an image build with that revision along with other submitted 
           revisions on other components under the image.
        """
        try:
            # Creating Request Detail
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}RequestDetailRequest')
            labelState = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}LabelState')

            request.LabelName = label_name
            request.ComponentName = component_name
            request.IuName = iu_name
            request.VersionedIuName = versioned_iu_name
            request.LabelPoc = label_poc
            request.Predecessor = predecessor
            request.ClientRoot = client_root
            request.CreatedBy = created_by
            request.State = labelState[state]
            request.IsActive = is_active
            request.IuClientId = iu_client_id
            request.ImageClientId = image_client_id

            # Assign PhNodeLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            phNodeLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}PhNodeLevel')
            request.IuLevel = phNodeLevel[iu_level]
            request.VersionedIuLevel = phNodeLevel[versioned_iu_level]

            # Assign LabelType Enum Value -> DirectAsset, PLFLabel,  CRMBuildId
            labelType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}LabelType')
            request.LabelType = labelType[label_type]

            # Assign LabelLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            labelLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}LabelLevel')
            request.LabelLevel = labelLevel[label_level]

            dependencyList = client.factory.create('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}ArrayOfstring')
            dependencyList.string = dependency_list
            request.DependencyList = dependencyList

            # Send Request
            logging.info("\nRequest:" + str(request))
            response = client.service.CreateRequest(request)
            logging.info("Response:" + str(response))
            return response

        except Exception as ex:
            logging.info("Exception:" + str(ex))


    def create_request_static_label_for_image(self,
                      versioned_iu_name,         # Image name or the Product name
                      versioned_iu_level,        # Product or Product line
                      iu_name,                   # Image name or the Product name
                      iu_level,                  # Product or Product line
                      label_name,                # Case sensitive string
                      label_type,                # Direct asset, PLFLabel, CRMBuildId
                      component_name,            # Productline/area/subsystem/unit
                      label_level,               # Product line, Area, Subsystem, Unit, Component
                      state,                     # Defined or Submitted
                      label_poc,                 # Multiple users are ok (comma separated)
                      created_by,                #
                      predecessor,               # Case sensitive string
                      client_spec,               # Mandatory for GLUE label submission or non-component label submission
                      client_spec_type,          # Baseline or File (Current ARIS only supports File as Cspec Type)
                      client_spec_p4_server,     #
                      client_spec_file_location, #
                      client_spec_file_version,  #
                      client_root,               #
                      is_active,                 #
                      iu_client_id=None,         # Name of the product variant when IuLevel is Product and LabelType is CRMBuildId
                      image_client_id=None,      # Variant. Required when LabelType is CRMBuildId and LabelLevel is ProductLine
                      dependency_list=None):     #

        """Create Request allows a user to create a single request with 
           either an existing or non-existing label. This method only supports 
           setting states with 'Defined' or 'Submitted'.
           
           Using create requests you can submit crm builds, component revisions 
           and perforce labels to Aris. For example if you have a component 
           revision on component c1 which belongs to software image I1, you can 
           create a request to submit the component revision on C1 to image I1. 
           This way the next aris assessment will pick up that component revision 
           and make an image build with that revision along with other submitted 
           revisions on other components under the image.
        """
        try:
            # Creating Request Detail
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}RequestDetailRequest')
            labelState = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}LabelState')
            
            request.LabelName = label_name
            request.ComponentName = component_name
            request.IuName = iu_name
            request.VersionedIuName = versioned_iu_name
            request.LabelPoc = label_poc
            request.Predecessor = predecessor
            request.ClientRoot = client_root
            request.CreatedBy = created_by
            request.State = labelState[state]
            request.IsActive = is_active
            request.IuClientId = iu_client_id
            request.ImageClientId = image_client_id
        
            # Assign PhNodeLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            phNodeLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}PhNodeLevel')
            request.IuLevel = phNodeLevel[iu_level]
            request.VersionedIuLevel = phNodeLevel[versioned_iu_level]
            
            # Assign LabelType Enum Value -> DirectAsset, PLFLabel,  CRMBuildId
            labelType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}LabelType')
            request.LabelType = labelType[label_type]
            
            # Assign LabelLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            labelLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}LabelLevel')
            request.LabelLevel = labelLevel[label_level]

            clientSpec = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}CodeBase')
            clientSpec.ClientSpecFileLocation = client_spec_file_location
            clientSpec.ClientSpecFileVersion = int(client_spec_file_version)
            clientSpec.ClientSpecP4Server = client_spec_p4_server
            
            # Assign CodeBaseType Enum Value ->  Baseline, File
            codeBaseType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}CodeBaseType')
            clientSpec.ClientSpecType = client_spec_type
            request.ClientSpec = clientSpec
            
            dependencyList = client.factory.create('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}ArrayOfstring')
            dependencyList.string = dependency_list
            request.DependencyList = dependencyList
            
            # Send Request
            logging.info("\nRequest:" + str(request))
            response = client.service.CreateRequest(request)
            logging.info("Response:" + str(response))
            return response

        except Exception as ex:
            logging.info("Exception:" + str(ex))


    def create_request(self,
                       versioned_iu_name,         # Image name or the Product name
                       versioned_iu_level,        # Product or Product line
                       iu_name,                   # Image name or the Product name
                       iu_level,                  # Product or Product line
                       label_name,                # Case sensitive string
                       label_type,                # Direct asset, PLFLabel, CRMBuildId
                       component_name,            # Productline/area/subsystem/unit
                       label_level,               # Product line, Area, Subsystem, Unit, Component
                       state,                     # Defined or Submitted
                       label_poc,                 # Multiple users are ok (comma separated)
                       created_by,                #
                       predecessor,               # Case sensitive string
                       client_spec,               # Mandatory for GLUE label submission or non-component label submission
                       client_spec_type,          # Baseline or File (Current ARIS only supports File as Cspec Type)
                       client_spec_p4_server,     #
                       client_spec_file_location, #
                       client_spec_file_version,  #
                       client_root,               #
                       is_active,                 #
                       iu_client_id=None,         # Name of the product variant when IuLevel is Product and LabelType is CRMBuildId
                       image_client_id=None,      # Variant. Required when LabelType is CRMBuildId and LabelLevel is ProductLine
                       dependency_list=None):     #

        """Create Request allows a user to create a single request with 
           either an existing or non-existing label. This method only supports 
           setting states with 'Defined' or 'Submitted'.
           
           Using create requests you can submit crm builds, component revisions 
           and perforce labels to Aris. For example if you have a component 
           revision on component c1 which belongs to software image I1, you can 
           create a request to submit the component revision on C1 to image I1. 
           This way the next aris assessment will pick up that component revision 
           and make an image build with that revision along with other submitted 
           revisions on other components under the image.
        """
        try:
            # Creating Request Detail
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}RequestDetailRequest')
            labelState = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}LabelState')
            
            request.LabelName = label_name
            request.ComponentName = component_name
            request.IuName = iu_name
            request.VersionedIuName = versioned_iu_name
            request.LabelPoc = label_poc
            request.Predecessor = predecessor
            request.ClientRoot = client_root
            request.CreatedBy = created_by
            request.State = labelState[state]
            request.IsActive = is_active
            request.IuClientId = iu_client_id
            request.ImageClientId = image_client_id
        
            # Assign PhNodeLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            phNodeLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}PhNodeLevel')
            request.IuLevel = phNodeLevel[iu_level]
            request.VersionedIuLevel = phNodeLevel[versioned_iu_level]
            
            # Assign LabelType Enum Value -> DirectAsset, PLFLabel,  CRMBuildId
            labelType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}LabelType')
            request.LabelType = labelType[label_type]
            
            # Assign LabelLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            labelLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}LabelLevel')
            request.LabelLevel = labelLevel[label_level]

            clientSpec = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}CodeBase')
            clientSpec.ClientSpecFileLocation = client_spec_file_location
            clientSpec.ClientSpecFileVersion = int(client_spec_file_version)
            clientSpec.ClientSpecP4Server = client_spec_p4_server
            
            # Assign CodeBaseType Enum Value ->  Baseline, File
            codeBaseType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}CodeBaseType')
            clientSpec.ClientSpecType = client_spec_type
            request.ClientSpec = clientSpec
            
            dependencyList = client.factory.create('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}ArrayOfstring')
            dependencyList.string = dependency_list
            request.DependencyList = dependencyList
            
            # Send Request
            logging.info("\nRequest:" + str(request))
            response = client.service.CreateRequest(request)
            logging.info("Response:" + str(response))
            return response

        except Exception as ex:
            logging.info("Exception:" + str(ex))


    def get_build_items_for_crm_build(self, user_name, crm_build_id):
        """Returns a list of build items for a given CRMBuildID."""
        try:
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}GetBuildItemsForCrmBuildRequest')
            request.CRMBuildId = crm_build_id
            request.UserName = user_name
            
            logging.info("\nRequest:" + str(request))
            response = client.service.GetBuildItemsForCrmBuild(request)
            logging.info("Response:" + str(response))
            return response
        
        except Exception as ex:
            logging.info("Exception:" + str(ex))

    
    def get_device_assessments_for_crm_build(self, user_name, crm_build_id):
        """GetDeviceAssessmentsForCrmBuildallows user get the list of 
           device assessments ran for a build.
        """
        try:
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}GetDeviceAssessmentsForCrmBuildRequest')
            request.UserName = user_name
            request.CrmBuildId = crm_build_id
            
            logging.info("\nRequest:" + str(request))
            response = client.service.GetDeviceAssessmentsForCrmBuild(request)
            logging.info("Response:" + str(response))
            return response
        
        except Exception as ex:
            logging.info("Exception:" + str(ex))

    
    def get_integration_line_active_composition(
            self,
            user_name,
            integration_line_name,
            integration_line_level,         # SoftwareProduct or SoftwareImage
            integration_line_client_id=None # (required for Software Product, not required for SoftwareImage)
           ):
        """ UpdateRequestState method all to change request state from 
        "Defined" to "Submitted" or vice versa. """
        try:
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}UpdateRequestStateRequest')
            integrationType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}IntegrationType')
            labelState = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}LabelState')
            
            request.UserName = user_name
            request.IntegrationLineLevel = integrationType[integration_line_level]
            request.IntegrationLineName = integration_line_name
            request.IntegrationLineClientId = integration_line_client_id
            
            logging.info("\nRequest:" + str(request))
            result = client.service.GetIntegrationLineActiveCompositionRequest(request)
            logging.info("Result:" + str(result))
            return result

        except Exception as ex:
            logging.info("Exception:" + str(ex))


    def get_label_details(self, label_name):
        """
        GetLabelDetails method allows user to retrieve all the requests associated to a particular label, 
        including software product/image they were defined/submitted to and corresponding dependencies.
        """
        try:
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}LabelDetailRequest')
            request.LabelName = label_name

            logging.info("\nRequest:" + str(request))
            response = client.service.GetLabelDetails(request)
            logging.info("Response:" + str(response))
            return response
        
        except Exception as ex:
            logging.info("Exception:" + str(ex))
        
    
    def get_last_assessment_detail(self,
                                user_name,
                                versioned_iu_name,
                                versioned_iu_level,
                                iu_name,
                                iu_level,
                                is_active,
                                is_passed,
                                assessment_type,
                                iu_client_id=None
                               ):
        """
        GetLastAssessmentDetail method allows user to find out what was last 
        success/failed assessment with Participated Labels with state.
        """
        try:
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}AssessmentDetailRequest')
        
            # Assign PhNodeLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            phNodeLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}PhNodeLevel')
    
            request.VersionedIuName = versioned_iu_name
            request.VersionedIuLevel = phNodeLevel[versioned_iu_level]
            request.IuName = iu_name
            request.IuClientId = iu_client_id
            request.IuLevel = phNodeLevel[iu_level]
            request.IsPassed = is_passed
            request.IsActive = is_active
            request.UserName = user_name
            request.AssessmentType = assessment_type

            logging.info("\nRequest:" + str(request))
            response = client.service.GetLastAssessmentDetail(request)
            logging.info("Response:" + str(response))
            return response
        
        except Exception as ex:
            logging.info("Exception:" + str(ex))

    
    def get_latest_labels(self, 
                          user_name,
                          iu_name,
                          iu_level,
                          iu_client_id=None,
                          state="All"):
        """
        GetLastLabels method allows a user to retrieve the latest labels submitted to a software image 
        or software product. In other words, the latest label for each component submitted to an image.
        *     If a submission state is specified for instance, Defined, Submitted, Rejected, Integrated, 
              etc then the method will the latest labels in that state.
        *     If the request contains a list of components, the response will only contains latest 
              labels for those components.
        """
        request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}GetLatestLabelsRequest')
        
        logging.debug("Request:" + str(request))
        request.UserName = user_name
        request.IntegrationUnitName = iu_name
        request.IntegrationUnitClientId = iu_client_id
        
        integrationType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}IntegrationType')
        logging.debug("IntegrationType:" + str(integrationType))
        request.IntegrationUnitLevel = integrationType[iu_level]

        labelState = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}LabelState')
        logging.debug("labelState:" + str(state))
        request.State = labelState[state]

        components = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}ArrayOfIntegrationUnitItemInfo')
        request.IntegrationUnitItems.IntegrationUnitItemInfo.append(components);
        
        logging.info("\nRequest:" + str(request))
        result = client.service.GetLastLabels(request)
        logging.info("Result:" + str(result))
        return result
    

    def reject_resubmitted_label(self,
                                 user_name,
                                 label_name,
                                 versioned_iu_name,
                                 versioned_iu_level,
                                 iu_name,
                                 iu_level,
                                 is_active,
                                 iu_client_id=None
                                ):
        """This method allows you to reject a previously resubmitted label"""
        try:
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}RejectResubmittedLabelRequest')
    
            phNodeLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}PhNodeLevel')

            request.UserName = user_name
            request.LabelName = label_name
            request.VersionedIuName = versioned_iu_name
            request.VersionedIuLevel = phNodeLevel[versioned_iu_level]
            request.IuName = iu_name
            request.IuClientId = iu_client_id
            request.IuLevel = phNodeLevel[iu_level]
            request.IsActive = is_active

            logging.info("\nRequest:" + str(request))
            response = client.service.RejectResubmittedLabelRequest(request)
            logging.info("Response:" + str(response))
            return response

        except Exception as ex:
            logging.info("Exception:" + str(ex))


    def resubmit_label(self,
                       user_name,
                       label_name,
                       versioned_iu_name,
                       versioned_iu_level,
                       iu_name,
                       iu_level,
                       is_active,
                       iu_client_id=None
                      ):

        """ReSubmitLabel method allows user to re-submit a Rejected label."""
        try:
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}ReSubmitLabelRequest')
    
            phNodeLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}PhNodeLevel')

            request.UserName = user_name
            request.LabelName = label_name
            request.VersionedIuName = versioned_iu_name
            request.VersionedIuLevel = phNodeLevel[versioned_iu_level]
            request.IuName = iu_name
            request.IuClientId = iu_client_id
            request.IuLevel = phNodeLevel[iu_level]
            request.IsActive = is_active

            logging.info("\nRequest:" + str(request))
            response = client.service.ReSubmitLabelRequest(request)
            logging.info("Response:" + str(response))
            return response
        
        except Exception as ex:
            logging.info("Exception:" + str(ex))


    def run_assessment(self,
                       user_name,
                       iu_name,           # Product or Software Image name
                       iu_level,          # "Product" or "ProductLine"
                       iu_client_id=None  # Present for a Product only
                      ):
        """ Run Assessment method allows users to run the assessment 
            for a particular software image or product.
        """
        try:
            request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}RunAssessmentRequest')
        
            # Assign PhNodeLevel Enum Value -> Product, ProductLine, Area, Subsystem, Unit, Component
            phNodeLevel = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Contracts}PhNodeLevel')
    
            request.IuName = iu_name
            request.IuLevel = phNodeLevel[iu_level]
            request.IuClientId = iu_client_id
            request.UserName = user_name
            
            logging.info("\nRequest:" + str(request))
            response = client.service.RunAssessment(request)
            logging.info("Response:" + str(response))
            return response
        
        except Exception as ex:
            logging.info("Exception:" + str(ex))

    
    def save_test_results(self,
                          user_name, 
                          testResultsJson,
                          assessmentId):
        """
        SaveTestResults method allows for saving the test results in 
        ARIS once all the tests have run.
        
            Input Parameters (* indicates required parameters)
                user_name *
                testResultsJson * (path of the test result json)
                assessmentId * (valid int > 0)
        
            Response Message 
                Success bool (indicate if request state is updated successfully)
                LogMessage string (any error message if failed to update request state)
        """
        try:
             if assessmentId < 1:
                  raise Exception ("Use a valid Assessment Id")
             if user_name is None or len(user_name) == 0:
                  raise Exception ("Use a valid user_name")
             #read the json
             with open (testResultsJson) as jsonFile:
                 text_data = jsonFile.read()
             #deserialize the json, if the json text is either invalid or empty json.loads takes care of it
             payload = json.loads(text_data)
             #theres no point saving the data if there's no data in the deserialized dict
             if len(payload) < 1 or (len(payload['CcTestResults']) < 1 and len(payload['EcTestResults']) < 1 and len(payload['AmTestResults']) < 1):
                  raise Exception("Json file could not be loaded properly.")
             url = 'http://hci/arisservice/arisexternalservice.svc?wsdl'
             client = Client(url)
             if len(payload['CcTestResults']) > 0:
                  for ccResult in payload['CcTestResults'] :
                       ccTestResultDetail = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}TestResultDetail');
                       ccTestResultDetail.AssessmentId = assessmentId
                       ccTestResultDetail.CrmBuildId = ccResult['CrmBuildId']
                       ccTestResultDetail.ExternalId = ccResult['ExternalTestId']
                       ccTestResultDetail.IsGated = ccResult['IsGated']
                       ccTestResultDetail.Link = ccResult['Link']
                       ccTestResultDetail.Name = ccResult['Name']
                       ccTestResultDetail.Result = ccResult['Result']
                       ccTestResultDetail.Status = ccResult['Status']
                       request.CcTestResults.CcTestResultDetail.append(ccTestResultDetail);
             else:
                  request.CcTestResults.CcTestResultDetail.append(client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}TestResultDetail'))


             if len(payload['EcTestResults']) > 0:
                  for ecResult in payload['EcTestResults'] :
                       ecTestResultDetail = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}TestResultDetail');
                       ecTestResultDetail.AssessmentId = assessmentId
                       ecTestResultDetail.CrmBuildId = ecResult['CrmBuildId']
                       ecTestResultDetail.ExternalId = ecResult['ExternalTestId']
                       ecTestResultDetail.IsGated = ecResult['IsGated']
                       ecTestResultDetail.Link = ecResult['Link']
                       ecTestResultDetail.Name = ecResult['Name']
                       ecTestResultDetail.Result = ecResult['Result']
                       ecTestResultDetail.Status = ecResult['Status']
                       request.EcTestResults.EcTestResultDetail.append(ecTestResultDetail);
             else:
                  request.EcTestResults.EcTestResultDetail.append(client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}TestResultDetail'))


             if len(payload['AmTestResults']) > 0:
                  for amResult in payload['AmTestResults'] :
                       amTestResultDetail = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}TestResultDetail');
                       amTestResultDetail.AssessmentId = assessmentId
                       amTestResultDetail.CrmBuildId = amResult['CrmBuildId']
                       amTestResultDetail.ExternalId = amResult['ExternalTestId']
                       amTestResultDetail.IsGated = amResult['IsGated']
                       amTestResultDetail.Link = amResult['Link']
                       amTestResultDetail.Name = amResult['Name']
                       amTestResultDetail.Result = amResult['Result']
                       amTestResultDetail.Status = ccResult['Status']
                       request.AmTestResults.AmTestResultDetail.append(ccTestResultDetail);
             else:
                  request.AmTestResults.AmTestResultDetail.append(client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}TestResultDetail'))
             response = client.service.SaveTestResults(request)
             print response

        except Exception as ex:
             print ex

    
    def save_test_results_v2(self):
        pass


    def update_request_state(self,
                             user_name,
                             label_name,
                             integration_line_name,
                             integration_line_level,   # SoftwareProduct or SoftwareImage
                             state,
                             integration_line_client_id=None # (required for Software Product, not required for SoftwareImage)
                            ):
        """ UpdateRequestState method all to change request state from 
            "Defined" to "Submitted" or vice versa. """
        request = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Web.Service.Requests}UpdateRequestStateRequest')
        integrationType = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}IntegrationType')
        labelState = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}LabelState')

        request.UserName = user_name
        request.LabelName = label_name
        request.IntegrationLineLevel = integrationType[integration_line_level]
        request.IntegrationLineName = integration_line_name
        request.IntegrationLineClientId = integration_line_client_id
        
        labelState = client.factory.create('{http://schemas.datacontract.org/2004/07/Qualcomm.Solana.Business.Entities.Enumerations}LabelState')
        logging.debug("labelState:" + str(state))
        request.RequestState = labelState[state]

        logging.info("\nRequest:" + str(request))
        result = client.service.UpdateRequestState(request)
        logging.info("Result:" + str(result))
        return result

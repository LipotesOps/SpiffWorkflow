from SpiffWorkflow.bpmn.serializer.BpmnSerializer import BpmnSerializer
from SpiffWorkflow.bpmn.serializer.Packager import Packager

from SpiffWorkflow.bpmn.specs.BpmnProcessSpec import BpmnProcessSpec
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow


packager_file = '/Users/abin/code/LipotesOps/lipotes-b/SpiffWorkflow/Action-Management.bpmn20.zip'
packager = Packager(packager_file, entry_point_process='Action Management')
bpmn_file = '/Users/abin/code/LipotesOps/lipotes-b/SpiffWorkflow/Action-Management.bpmn20.xml'

packager_file = '/Users/abin/code/LipotesOps/lipotes-b/SpiffWorkflow/Messages.bpmn20.zip'
packager = Packager(packager_file, entry_point_process='Messages')
bpmn_file = '/Users/abin/code/LipotesOps/lipotes-b/SpiffWorkflow/Messages.bpmn20.xml'

packager.add_bpmn_file(bpmn_file)
packager.create_package()

packager_data = open(packager_file, 'rb').read()
serializer = BpmnSerializer()

wf_spec = serializer.deserialize_workflow_spec(packager_data, filename=packager_file)
wf = BpmnWorkflow(wf_spec)

pass
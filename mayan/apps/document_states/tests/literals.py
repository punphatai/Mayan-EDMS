from ..literals import FIELD_TYPE_CHOICE_CHAR, WORKFLOW_ACTION_ON_ENTRY

TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_DOTTED_PATH = 'mayan.apps.document_states.workflow_actions.DocumentPropertiesEditAction'
TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEXT_LABEL = 'new document label'
TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEXT_DESCRIPTION = 'new document description'
TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEXT_DATA = {
    'document_label': TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEXT_LABEL,
    'document_description': TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEXT_DESCRIPTION
}
TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEMPLATE_LABEL = '{{ document.label }} new'
TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEMPLATE_DESCRIPTION = '{{ document.label }}'
TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEMPLATE_DATA = {
    'document_label': TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEMPLATE_LABEL,
    'document_description': TEST_DOCUMENT_EDIT_WORKFLOW_ACTION_TEMPLATE_DESCRIPTION
}

TEST_INDEX_LABEL = 'test workflow index'

TEST_HEADERS_KEY = 'test key'
TEST_HEADERS_VALUE = 'test value'
TEST_HEADERS_JSON = '{{"{}": "{}"}}'.format(
    TEST_HEADERS_KEY, TEST_HEADERS_VALUE
)
TEST_HEADERS_JSON_TEMPLATE_KEY = 'test key'
TEST_HEADERS_JSON_TEMPLATE_VALUE = '{{ document.label }}'
TEST_HEADERS_JSON_TEMPLATE = '{{"{}": "{}"}}'.format(
    TEST_HEADERS_JSON_TEMPLATE_KEY, TEST_HEADERS_JSON_TEMPLATE_VALUE
)
TEST_HEADERS_AUTHENTICATION_KEY = 'Authorization'
TEST_HEADERS_AUTHENTICATION_VALUE = 'Basic dGVzdHVzZXJuYW1lOnRlc3RwYXNzd29yZA=='
TEST_PAYLOAD_JSON = '{"label": "label"}'
TEST_PAYLOAD_TEMPLATE_DOCUMENT_LABEL = '{"label": "{{ document.label }}"}'
TEST_SERVER_USERNAME = 'testusername'
TEST_SERVER_PASSWORD = 'testpassword'

TEST_WORKFLOW_LABEL = 'test workflow label'
TEST_WORKFLOW_INTERNAL_NAME = 'test_workflow_label'
TEST_WORKFLOW_LABEL_EDITED = 'test workflow label edited'
TEST_WORKFLOW_INITIAL_STATE_LABEL = 'test initial state'
TEST_WORKFLOW_INITIAL_STATE_COMPLETION = 33
TEST_WORKFLOW_INSTANCE_LOG_ENTRY_COMMENT = 'test workflow instance log entry comment'
TEST_WORKFLOW_STATE_ACTION_LABEL = 'test state action label'
TEST_WORKFLOW_STATE_ACTION_WHEN = WORKFLOW_ACTION_ON_ENTRY
TEST_WORKFLOW_STATE_LABEL = 'test state label'
TEST_WORKFLOW_STATE_LABEL_EDITED = 'test state label edited'
TEST_WORKFLOW_STATE_COMPLETION = 66
TEST_WORKFLOW_TRANSITION_FIELD_HELP_TEXT = 'test workflow transition field help test'
TEST_WORKFLOW_TRANSITION_FIELD_LABEL = 'test workflow transition field'
TEST_WORKFLOW_TRANSITION_FIELD_NAME = 'test_workflow_transition_field'
TEST_WORKFLOW_TRANSITION_FIELD_TYPE = FIELD_TYPE_CHOICE_CHAR
TEST_WORKFLOW_TRANSITION_LABEL = 'test transition label'
TEST_WORKFLOW_TRANSITION_LABEL_2 = 'test transition label 2'
TEST_WORKFLOW_TRANSITION_LABEL_EDITED = 'test transition label edited'

TEST_INDEX_TEMPLATE_METADATA_EXPRESSION = '{{{{ document.workflow.{}.get_current_state }}}}'.format(
    TEST_WORKFLOW_INTERNAL_NAME
)

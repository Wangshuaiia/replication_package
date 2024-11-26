# To be used in APIPropertyRetriever signature
API_CAN_INPUT_EXAMPLE = {
    "ABCObject::valueOne": "CANSignal1",
    "ABCObject::valueFour::TRUE": "AASignal:BB OR PV_AnotherSignal:CC",
    "ABCObject::valueFour::False": "AASignal:AA",}

API_CAN_OUTPUT_EXAMPLE = [
    {"api_property": "valueOne", "can_signals": [{"can_name": "CanSignal1"}]},
	{"api_property": "valueFour","can_signals": [{
                "can_name": "AASignal",
                "can_mappings": [
                    {"api_value": "true", "can_value": ["BB"]},
                    {"api_value": "false", "can_value": ["AA"]},],},
            {"can_name": "PV_AnotherSignal",
                "can_mappings": [{"api_value": "true", "can_value": ["CC"]}],},],}
]

CAN_DATA_EXAMPLE = {"Abc_Mode": 1, "Ccd_Spare": 4}

API_CAN_LIST_EXAMPLE = [
    {"api_value": "true", "can_value": ["Mode"]},
    {"api_value": "false", "can_value": ["Spare"]},
]

API_CAN_VV_OUTPUT_EXAMPLE = [
    {"api_value": "true", "vv_value": 1},
    {"api_value": "false", "vv_value": 4},
]

SWAGGER_TO_CAN_ENUM_EXAMPLES = [
    {
        "api_data": {
            "isXEnabled": {
                "type": "boolean",
                "description": "Enables/disables the X function in the vehicle",
            }
        },
        "can_data": {
            "DeactivatedActivated2bit_Activated": 0,
            "DeactivatedActivated2bit_Deactivated": 1,
            "DeactivatedActivated2bit_Error": 2,
            "DeactivatedActivated2bit_NotAvailable": 3,
        },
        "api_can_mapping": [
            {"api_value": "false", "vv_value": 1},
            {"api_value": "true", "vv_value": 0},
        ],
    }
]

UNIT_EXAMPLE = [
    {"api_property": "propertyA", "api_unit": "Seconds"},
    {"api_property": "propertyB", "api_unit": "Watt-hours per 100 kilometers"},
]

UNITS = [
    "Minutes",
    "Seconds",
    "Hours"
]
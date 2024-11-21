# To be used in APIPropertyRetriever signature
YAML_CAN_INPUT_EXAMPLE = {
    "ABCObject::valueOne": "CANSignal1",
    "ABCObject::valueTwo::Sussy": "CANSignal2::Sus",
    "ABCObject::valueTwo::DefinitelyNotSussy": "CANSignal2::NotSus",
    "ABCObject::valueThree": "BA_CanSignal_XX Inverted signal.",
    "ABCObject::valueFour::TRUE": "AASignal:BB OR PV_AnotherSignal:CC",
    "ABCObject::valueFour::False": "AASignal:AA",
}

YAML_CAN_OUTPUT_EXAMPLE = [
    {"api_property": "valueOne", "can_signals": [{"can_name": "CanSignal1"}]},
    {
        "api_property": "valueTwo",
        "can_signals": [
            {
                "can_name": "CanSignal2",
                "can_mappings": [
                    {"api_value": "Sussy", "can_value": ["Sus"]},
                    {"api_value": "DefinitelyNotSussy", "can_value": ["NotSus"]},
                ],
            }
        ],
    },
    {
        "api_property": "valueThree",
        "can_signals": [
            {"can_name": "BA_CanSignal_XX", "optional_description": "Inverted signal."}
        ],
    },
    {
        "api_property": "valueFour",
        "can_signals": [
            {
                "can_name": "AASignal",
                "can_mappings": [
                    {"api_value": "true", "can_value": ["BB"]},
                    {"api_value": "false", "can_value": ["AA"]},
                ],
            },
            {
                "can_name": "PV_AnotherSignal",
                "can_mappings": [{"api_value": "true", "can_value": ["CC"]}],
            },
        ],
    },
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
    },
    {
        "api_data": {
            "preConditionsToAdjustDimming": {
                "type": "string",
                "enum": ["WRONG_VEHICLE_MODE", "POSITION_LIGHTS_NOT_ON"],
                "description": " Specify the condition which needs to be fulfilled to adjust X",
                "readOnly": "true",
            }
        },
        "can_data": {
            "PS_DimmingLevelStat_Adjustable": 0,
            "PS_DimmingLevelStat_NotAdjustableWrongVehicleMode": 1,
            "PS_DimmingLevelStat_NotAdjustablePositionLightsOff": 2,
            "PS_DimmingLevelStat_NotAvailable": 3,
        },
        "api_can_mapping": [
            {"api_value": "WRONG_VEHICLE_MODE", "vv_value": 1},
            {"api_value": "POSITION_LIGHTS_NOT_ON", "vv_value": 2},
        ],
    },
]

UNIT_EXAMPLE = [
    {"api_property": "propertyA", "api_unit": "Seconds"},
    {"api_property": "propertyB", "api_unit": "Watt-hours per 100 kilometers"},
]

UNITS = [
    "Minutes",
    "Seconds",
    "Hours",
    "Milliliters per 100 kilometers",
    "Millimeters",
    "Revolutions",
    "Degrees Celsius",
    "Radians",
    "Pascals per second",
    "Meters",
    "Kilometers",
    "Watts",
    "Liters",
    "Liters per hour",
    "Radians per second",
    "Meters per second squared",
    "Miles per gallon",
    "Amperes",
    "Watts per hour",
    "Watt-hours per 100 kilometers",
    "Degrees",
    "Kilowatt-hours",
    "Kilometers per liter",
    "Kilopascals",
    "Kilograms",
    "Years",
    "Percent",
    "Months",
    "Days",
    "Grams per 100 kilometers",
    "Hz",
    "RPM",
    "Kilometers per hour",
]
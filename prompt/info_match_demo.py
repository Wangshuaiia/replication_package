import dspy
import os
from signature_data import APIToCANSignalMapper, YAML_CAN_INPUT_EXAMPLE, YAML_CAN_OUTPUT_EXAMPLE


# Initialize the OpenAI language model
os.environ['OPENAI_API_KEY'] = 'your_openai_api_key'
lm = dspy.OpenAI(model='gpt-4o-mini')
dspy.settings.configure(lm=lm)

    
if __name__ == '__main__':
    # Descriptive API property names and CAN signal
    YAML_DEMO_LIST = [
        "engineTemperature",  
        "brakeStatus",
        "batteryLevel",
        "doorLock",
        "headlightStatus"
    ]
    
    CAN_DEMO_LIST = [
        "Engine_Temperature::Celsius", 
        "Brake_Status::Engaged/Disengaged",  
        "Battery_Level::Percentage",  
        "Door_Lock::Locked/Unlocked",  
        "Headlight_Status::On/Off"  
    ]

    # Create a DSPy module
    api_property_to_can_signal = dspy.TypedChainOfThought(APIToCANSignalMapper)

    # Run the module
    prediction = api_property_to_can_signal(
        api_table_example=YAML_CAN_INPUT_EXAMPLE,
        api_to_can_mapping_example=YAML_CAN_OUTPUT_EXAMPLE,
        api_to_can_dict=dict(zip(YAML_DEMO_LIST, CAN_DEMO_LIST)),
    )
    result = prediction.mapped_api_to_can

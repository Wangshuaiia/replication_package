import dspy
import os
from signature_data import API_CAN_INPUT_EXAMPLE, API_CAN_OUTPUT_EXAMPLE
from spapi_signatures import APIPropertyToCANSignal

# Initialize the OpenAI language model
os.environ['OPENAI_API_KEY'] = 'your_openai_api_key'
lm = dspy.OpenAI(model='gpt-4o')
dspy.settings.configure(lm=lm)


if __name__ == '__main__':
    # Descriptive API property names and CAN signal
    APIProperty_DEMO_LIST = [
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
    api_property_to_can_signal = dspy.TypedChainOfThought(APIPropertyToCANSignal)

    # Run the module
    prediction = api_property_to_can_signal(
        api_table_example=API_CAN_INPUT_EXAMPLE,
        api_to_can_mapping_example=API_CAN_OUTPUT_EXAMPLE,
        api_to_can_dict=dict(zip(APIProperty_DEMO_LIST, CAN_DEMO_LIST)),
    )
    result = prediction.mapped_api_to_can

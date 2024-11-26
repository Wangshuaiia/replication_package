import dspy
import os
from spapi_signatures import APIObjectGeneratorSignature
# Initialize the OpenAI language model
os.environ['OPENAI_API_KEY'] = 'your_openai_api_key'
lm = dspy.OpenAI(model='gpt-4o')
dspy.settings.configure(lm=lm)

reasoning_prefix = """Reasoning: Let's think step by step to determine the values for the API properties.
The strategy is as follows:
1. Identify dependencies and logical rules based on the descriptions and shared CAN signals in the API specification:
   - Determine if multiple properties share the same CAN signal, indicating dependency.
   - Identify logical dependencies, such as properties affecting each other (e.g., a property setting the unit for another).
   - Define the order in which dependent properties should be decided.
   - Ensure that properties sharing the same CAN signal are logically consistent.
2. Determine the type of the API property (e.g., string, number).
   2.1 If it's ID related, retrieve it directly from the example provided.
   2.2 For strings, respect formats like date-time or enums and generate a random value accordingly.
   2.3 For numbers, derive a value using 'can_min', 'can_max', 'can_resolution', ensuring consistency if there are unit conversions. Pick a value that aligns with the specified resolution (if applicable), avoiding examples when 'can_min' and 'can_max' are available.
3. If there is no mapping to a CAN signal, use the provided example or assign an appropriate value based on the property type.
4. Assign values to properties while maintaining logical consistency:
   - For properties sharing CAN signals, ensure that their values are logically coherent.
   - Apply logical rules from property descriptions to avoid invalid combinations.
   - Maintain consistency in properties influenced by the same CAN value.
"""

reasoning = dspy.OutputField(
    prefix=reasoning_prefix,
    desc="Use the reasoning steps to generate a valid API object. Begin by evaluating the first API property...",
)


class APIObjectGenerator(dspy.Module):
    def __init__(self, llm):
        super().__init__()
        self.llm = llm
        self._gen_api_object = dspy.TypedChainOfThought(
            APIObjectGeneratorSignature, reasoning=reasoning
        )

    def forward(
        self,
        api_object,
        yaml_can,
        api_spec,
    ):
        """
        Generates an API object with valid values for the API properties.

        Args:
            api_object (dict): The initial API object with potential null properties.
            yaml_can (dict): The YAML CAN mappings containing the relationships to CAN signals.
            api_spec (dict): The API specification detailing property requirements.

        Returns:
            dict: The completed API object with null properties filled in based on rules and mappings.
        """
        with dspy.context(lm=self.llm):
            api_object = self._gen_api_object(api_spec, yaml_can).api_object
        return api_object


if __name__ == '__main__':
    # Example input data
    api_object_to_fill = {
        "isAuxiliaryHeaterActivated": None
    }
    
    api_specification = {
        "ClimateObject": {
            "type": "object",
            "description": "Manipulate climate settings on the truck.",
            "required": [
                "type"
            ],
            "properties": {
                "acMode": {
                    "type": "string",
                    "enum": ["STANDARD", "ECONOMY"]
                },
                "autoFanLevel": {
                    "type": "string",
                    "enum": ["LOW", "NORMAL", "HIGH"]
                },
                "isAuxiliaryHeaterActivated": {
                    "type": "boolean"
                }
            }
        }
    }
    
    api_prop_to_can_signal_mappings = {
        "ClimateObject": [
            {
                "api_property": "acMode",
                "api_property_mappings": {
                    "can_signal": "APIACModeRqst",
                    "vv_state": "apiacmode_rqst"
                },
                "api_value_mappings": [
                    {
                        "api_value": "ECONOMY",
                        "can_value": "LOW",
                        "vv_state_value": "1"
                    },
                    {
                        "api_value": "STANDARD",
                        "can_value": "HIGH",
                        "vv_state_value": "2"
                    }
                ]
            }
        ]
    }
    
    previously_generated_api_objects = []

    # Create an instance of APIObjectGenerator
    api_object_generator = APIObjectGenerator(lm)

    # Generate the API object
    filled_api_object = api_object_generator.forward(
        api_object=api_object_to_fill,
        yaml_can=api_prop_to_can_signal_mappings,
        api_spec=api_specification
    )

    # Print the result
    print("Generated API Object:", filled_api_object)

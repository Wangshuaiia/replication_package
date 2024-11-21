import dspy


reasoning_prefix = """Reasoning: Let's think step by step to generate the values for the API properties.
The strategy is the following:
1. Identify dependencies and logical rules based on descriptions and shared CAN signals in the API specification:
   - If multiple properties share the same CAN signal, they are dependent.
   - Identify logical dependencies described in the property descriptions, such as a property setting the unit for another property.
   - Document the order in which dependent properties should be decided.
   - Specifically, if a CAN signal implies certain states for multiple properties, those properties must be logically consistent with each other.
2. Determine the type of the API property e.g. string, number. If it's ID related, skip the substeps below and get it directly from the example provided in the API specification
2.1 When string, respect the format (date-time, enum etc.). Pick a random value.
2.2 When number, pick a number according to the corresponding 'can_min', 'can_max', 'can_resolution' and scale it accordingly if 'api_unit' and 'can_unit' are not the same. Ensure the number picked is a multiple of the resolution (if there is a resolution). Do not pick the example if there exist a can_min and a can_max.
3. If there is no mapping to a CAN signal (can_name value), pick the example. If there's no example, set it to an appropriate value according to the property type.
4. Set values for properties based on dependencies and logical rules in the correct order:
   - For properties sharing the same CAN signal, determine their values based on logical consistency and dependency rules. Pay extra attention to the CAN value of API properties sharing the same CAN signal.
   - Apply logical rules from the property descriptions to maintain consistency among dependent properties. Specifically:
     - Ensure that if a property value implies a specific CAN state, then other properties dependent on the same CAN signal are set accordingly.
     - Recognize that certain combinations of property values may be logically invalid due to CAN signal mappings, preventing conflicting API property values.
     - For instance, ensure that if a CAN signal associates different states to different API properties, these properties' values must match that CAN value consistently.
"""

reasoning = dspy.OutputField(
    prefix=reasoning_prefix,
    desc="To produce the api_object, we will use the strategy. The first API property is ...",
)


class APIObjectGeneratorSignature(dspy.Signature):
    """
    Generate a valid API object by filling in ONLY the null values for API properties based on API specification and the mappings to CAN signals.
    """

    api_object_to_fill: dict = dspy.InputField(
        desc="The API object to modify by filling ONLY null the values"
    )
    api_specification: dict = dspy.InputField(
        desc="Contains information about the API properties"
    )
    api_prop_to_can_signal_mappings: dict = dspy.InputField(
        desc="Contains mapping information from each API property to the corresponding CAN signal(s)"
    )

    previously_generated_api_objects: list = dspy.InputField(
        desc="Previously generated API objects. To be used to generate a new API object with a different configuration from the previous ones."
    )
    api_object: dict = dspy.OutputField(desc="API object filled in with valid values")


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
        Generates an API object with values for the API properties.

        Args:
            api_object (dict): The initial API object.
            yaml_can (dict): The YAML CAN mappings.
            api_spec (dict): The Swagger specification of the API object.

        Returns:
            dict: The generated API object with filled values.
        """
        with dspy.context(lm=self.llm):
            api_object = self._gen_api_object(api_spec, yaml_can).api_object
        return api_object

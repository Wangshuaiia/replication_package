import dspy

class APIPropertyToCANSignal(dspy.Signature):
    """    
    Given an API table and an API property -> CAN signal map, generate a list of API properties -> CAN signal(s). 
    """

    api_to_can_dict: dict = dspy.InputField(
        desc="Dictionary containing mappings between API properties and their corresponding CAN signals. The CAN signal format can be snake_case or CamelCase. Descriptive details after '::' represent possible mapping details."
    )
    api_table_example: dict = dspy.InputField(desc="Example input table containing API properties.")
    api_to_can_mapping_example: list[dict] = dspy.InputField(
        desc="Example of API property-to-CAN signal mappings. The CAN signal name typically includes optional descriptive information after '::'. Only the part before '::' is the signal name."
    )
    mapped_api_to_can: list = dspy.OutputField(
        desc="List of mappings between API properties and their respective CAN signals."
    )


class CANValueMapper(dspy.Signature):
    """
    Given a dictionary of CAN signal mappings and corresponding integer values, mapping CAN signal values with their best-fit integer representations.
    """

    can_value_mapping_example: dict = dspy.InputField(desc="Example of CAN signal to integer value mapping.")
    api_to_can_list_example: list[dict] = dspy.InputField(desc="Example of API property to CAN signal mappings.")
    replaced_output_example: list[dict] = dspy.InputField(
        desc="The resulting mappings must follow a format similar to the example provided."
    )
    can_values: dict = dspy.InputField(desc="Dictionary mapping CAN signals to their respective integer values.")
    api_to_can_list: list = dspy.InputField(desc="List of API property to CAN signal mappings.")
    mapped_api_to_can_values: list = dspy.OutputField(
        desc="List containing API property mappings updated with the appropriate integer CAN signal values."
    )


class VirtualVehicleAttributeSetter(dspy.Signature):
    """
    Generate values for Virtual Vehicle (VV) attributes based on API property mappings and their assigned values.
    If a unit is provided, determine the unit from either the API property description or its name and set the VV attribute value accordingly.
    """

    api_values: dict = dspy.InputField(
        desc="Dictionary where keys are API properties and values are the corresponding assigned values."
    )
    api_to_vv_mapping: dict = dspy.InputField(
        desc="Dictionary containing mapping information between API properties and VV attributes, including optional details such as min, max, and units."
    )
    vv_attribute_values: dict = dspy.OutputField(
        desc="Dictionary where keys are VV attributes and values are set based on API property values."
    )


class SwaggerToCANMapper(dspy.Signature):
    """
    Given an API property, map its values to the most appropriate CAN definition.
    """

    mapping_example: list[dict] = dspy.InputField(
        desc="Example mapping of API properties to CAN definitions, which must follow the same format as 'api_to_can_mapping'."
    )
    api_property_info: dict = dspy.InputField(
        desc="Information about API property, including type, description, and example values."
    )
    can_definitions: dict = dspy.InputField(
        desc="Dictionary of CAN definitions and their respective values."
    )
    api_to_can_mapping: list = dspy.OutputField(
        desc="List mapping API properties to CAN definitions based on the best fit."
    )


class APIUnitRetriever(dspy.Signature):
    """
    Given information about API properties, attempt to derive the unit for each property, typically based on its name or description.
    If no explicit unit is available, it should be omitted from the output.
    """

    allowed_units: list = dspy.InputField(
        desc="List of permissible unit values to assign to the API properties."
    )
    expected_output_example: list[dict] = dspy.InputField(
        desc="Expected output format, including potential units for API properties (or empty if not applicable)."
    )
    api_property_details: dict = dspy.InputField(
        desc="Details about API properties, including name and description."
    )
    api_property_units: list[dict] = dspy.OutputField(
        desc="List of dictionaries, where each contains the API property name and its derived unit. If a property lacks a unit, it should not be included."
    )


class APIObjectGeneratorSignature(dspy.Signature):
    """
    Generate a valid API object by filling in the null values for the API properties based on the given API specification and CAN signal mappings.
    """

    api_object_to_fill: dict = dspy.InputField(
        desc="The API object with null values that need to be filled based on the specification and mappings."
    )
    api_specification: dict = dspy.InputField(
        desc="The API specification, including details of each property and their dependencies."
    )
    api_prop_to_can_signal_mappings: dict = dspy.InputField(
        desc="Mapping details between API properties and CAN signals, providing the relationship for value generation."
    )

    previously_generated_api_objects: list = dspy.InputField(
        desc="List of previously generated API objects, used to ensure the generated object is distinct from previous versions."
    )
    api_object: dict = dspy.OutputField(desc="The resulting API object with all null values filled appropriately.")

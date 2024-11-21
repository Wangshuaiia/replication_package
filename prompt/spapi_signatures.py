import dspy

class APIPropertyToCANSignal(dspy.Signature):
    """
    Given an API table and an API property -> CAN signal map, generate a list of API properties -> CAN signal(s).
    """

    input_example: dict = dspy.InputField()
    output_example: list[dict] = dspy.InputField(
        desc="Fill in the optional description if there is any additional information available that may be useful. The CAN mapping typically exists when the API property is a boolean. Keep in mind that EVERYTHING after :: is not a part of the CAN signal name, but a part of the possible mapping."
    )
    api_properties_to_can_dict: dict = dspy.InputField(
        desc="A dictionary containing the mappings between an API attribute and its corresponding CAN signal. The CAN signal is typically in the form of {x}_{y} or {x}_{y}_{z}, but may also be in one CamelCase string. The choices for a CAN signal is AFTER the :: part of the signal, and contains the mapping between the API property and its choice value within the CAN signal."
    )
    api_prop_to_can: list = dspy.OutputField(
        desc="A list of API properties, with corresponding CAN signals."
    )


class APIPropertyToCANValueSignature(dspy.Signature):
    """
    Given a dictionary of mappings between a CAN signal and its integer representation, replace the can_values in the API -> CAN map with the integer value that fits best. No value is allowed to be left as null.
    """

    can_data_example: dict = dspy.InputField()
    api_can_list_example: list[dict] = dspy.InputField()
    output_example: list[dict] = dspy.InputField(
        desc="The result HAS to adhere to a similar format as the example output"
    )
    can_data: dict = dspy.InputField()
    api_can_list: list = dspy.InputField()
    api_can_vv_integer: list = dspy.OutputField()


class VVAttributeSetterSignature(dspy.Signature):
    """
    Generate integer values for the provided Virual Vehicle States (VV) based on corresponding API Property mappings and values set for them.
    If vv_unit is present, detect the unit of the corresponding API property from "api_unit" key or through its name and set the VV attribute value accordingly.
    """

    api_properties_and_values: dict = dspy.InputField(
        desc="A dictionary where the keys are the API properties and the values are the corresponding assigned values"
    )
    api_vv_mappings: dict = dspy.InputField(
        desc="A dictionary containing information about mapping between API properties of objects and VV attributes, and optionally the minimum, maximum and units of VV attribute, and units of API property"
    )
    vv_values: dict = dspy.OutputField(
        desc="A dictionary where a key is a VV attribute and the value is corresponding value assigned based on the assigned API property value"
    )


class SwaggerToCANEnumValueSignature(dspy.Signature):
    """
    Given an API property, map its values to the value of the CAN definition that fits best
    """

    input_output_examples: list[dict] = dspy.InputField(
        desc="The output HAS to adhere to a similar format as 'api_can_mapping'"
    )
    api_prop_info: dict = dspy.InputField(
        desc="Information about the API property data such as type, description and example"
    )
    can_data: dict = dspy.InputField(desc="CAN definitions and their respective values")
    api_can_mapping: list = dspy.OutputField()


class APIUnitRetrieverSignature(dspy.Signature):
    """
    Given information about API properties, attempt to retrieve the unit of the API properties.
    Usually, the unit can be derived from the name or the description of the API property.
    Note that in most cases there is no explicit unit so you should not include it in the output.
    """

    unit_list: list = dspy.InputField(
        desc="A strict list of values that you can set the units to."
    )
    output_example: list[dict] = dspy.InputField(
        desc="Expected output (or empty if not applicable)"
    )
    api_info: dict = dspy.InputField(desc="Information about API properties.")
    api_property_units: list[dict] = dspy.OutputField(
        desc="A list of dictionaries where each dictionary contains information about the API property name and the unit. If API property does not have a corresponding unit, do not include it in the dictionary"
    )


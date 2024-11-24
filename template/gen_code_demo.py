from jinja2 import Environment, FileSystemLoader

# Directory where the template file is located
template_directory = './'  # Ensure this path matches the template file location
template_file = 'get.py.jinja'

# Data required for rendering
data = {
    "vv_attributes": {
        "speed": 120,
        "fuel_level": 75
    },
    "endpoint_path": "/v1/vehicle/status",
    "request_headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer some_token"
    },
    "api_object": {
        "status": "active",
        "fuel_level": 75
    }
}

# Custom filter: retain the data type
def keeptype(value):
    if isinstance(value, str):
        return f'"{value}"'
    return value

# Set up Jinja environment
file_loader = FileSystemLoader(template_directory)
env = Environment(loader=file_loader)
env.filters['keeptype'] = keeptype  # Register the custom filter

# Load and render the template
template = env.get_template(template_file)
rendered_code = template.render(data)

# Print the generated test code
print(rendered_code)

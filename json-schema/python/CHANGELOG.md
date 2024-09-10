# 0.0.1
- Introduced generating of pydantic classes out of JSON schemas.

# 0.1.0
- Added JSON schema and generated pydantic class for performance-monitoring service.

# 0.1.1
- Updated generated pydantic classes with bunmped version
  of datamodel-code-generator (0.25.5).

# 0.2.0
- Added JSON schema and generated pydantic class for device GeoLocation.

# 0.2.1
- Added Kafka header 'type' constant into header_constants module.

# 0.2.2
- Make Enum as subclass for JSON serialising.

# 0.3.0
- Added JSON schema and generated pydantic class for unified performance-message notifications.
- Added cpu-usage and memory-usage header constants for performance-message notifications.

# 0.3.1
- Package dependency update

# 0.4.0
- Added a 'path' field into performance-notifications json schema.
- Changed a 'metrics' field type in performance-message json schema from Any to Dict.
- Added a new Kafka header constant 'interface-utilization' to the header_constants module.

# 0.4.1
- split a Kafka header constant 'interface-utilization' to 'interface-ipv4-utilization' and 'interface-ipv6-utilization'

# 0.4.2
- Bump dependencies.

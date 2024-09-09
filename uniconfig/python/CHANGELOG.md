# 0.1.0
- Upgrade pydantic version to v2

# 0.1.1
- Float/Int mismatch fix
- Uniconfig 5.1.16

# 1.0.0
- FM 6.0.0.

# 1.1.0
- Compatibility with UniConfig 6.0.X.
- Added missing gNMI installation parameters.
- Added missing SNMP installation parameters.
- Fixed generation of arrays with null type
  (added --strict-nullable attribute).
- Bumped version of datamodel-code-generator to 0.25.5.

# 1.1.1
- Introduction of custom git patches for generated UniConfig models.
- Added UniConfig patches:
  1. ignore createsubscription ruff errors
  2. fix discover address spell error
  3. fix generated port constraints in discover model

# 1.2.0
- Update models based on new OpenAPI fixed in UniConfig 6.1.x

# 1.2.1
- Package dependency update

# 2.0.0
- Update models based on the UniConfig 7.0.0 OpenAPI.

# 2.0.1
- Fix version in the RELEASE.md.

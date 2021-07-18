# JSON Schema — Extended 🎆

[![Maintainability](https://api.codeclimate.com/v1/badges/52750b29e206aa505f0a/maintainability)](https://codeclimate.com/github/janw/jsonschema-extended/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/52750b29e206aa505f0a/test_coverage)](https://codeclimate.com/github/janw/jsonschema-extended/test_coverage)

The jsonschema-extended library (JSE) provides an extended version of JSON Schema functionality as provided by the [`jsonschema` package](https://github.com/Julian/jsonschema). JSE by default enables all current and previous format validators (independent of the JSON Schema draft they were introduced or removed for) for the latest draft version, and includes a variety of additional format validators that are not included in the JSON schema spec.

I created JSE to use it in the configuration validation in another project of mine, [CleanAB](https://github.com/janw/cleanab), which requires more "niche" data types to be checked for, as well as default values. The latter is also supported by JSE right out of the box.

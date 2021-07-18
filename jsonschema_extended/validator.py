from functools import partial

from jsonschema import validators

from .format_checker import extended_format_checker

LATEST_VERSION = validators.Draft7Validator


def extend_with_default(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

        yield from validate_properties(
            validator,
            properties,
            instance,
            schema,
        )

    return validators.extend(
        validator_class,
        {"properties": set_defaults},
    )


def create_validator(
    validator_class=LATEST_VERSION, format_checker=extended_format_checker
):
    return partial(
        extend_with_default(validator_class),
        format_checker=format_checker,
    )


ExtendedValidator = create_validator()

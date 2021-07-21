# JSON Schema — Extended 🎆

[![Maintainability](https://api.codeclimate.com/v1/badges/52750b29e206aa505f0a/maintainability)](https://codeclimate.com/github/janw/jsonschema-extended/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/52750b29e206aa505f0a/test_coverage)](https://codeclimate.com/github/janw/jsonschema-extended/test_coverage)

The jsonschema-extended library (JSE) provides an extended version of JSON Schema functionality as provided by the [`jsonschema` package](https://github.com/Julian/jsonschema). JSE by default enables all current and previous format validators (independent of the JSON Schema draft they were introduced or removed for) for the latest draft version, and includes a variety of additional format validators that are not included in the JSON schema spec.

I created JSE to use it in the configuration validation in another project of mine, [CleanAB](https://github.com/janw/cleanab), which requires more "niche" data types to be checked for, as well as default values. The latter is also supported by JSE right out of the box.

## What is "extended" about it?

* Format validation is enabled by default
* Most formats of all JSON schema draft versions are enabled out-of-the-box (independent of what version they were actually specified in), namely:
  * `color`
  * `date`
  * `date-time`
  * `email`
  * `hostname`
  * `idn-email`
  * `idn-hostname`
  * `ipv4`
  * `ipv6`
  * `json-pointer`
  * `regex`
  * `relative-json-pointer`
  * `time`
  * `uri`
  * `uri-reference`
  * `uuid`
* Additonal general purpose formats have been added:
  * `color3`: [CSS3 color names](https://www.w3.org/TR/2018/REC-css-color-3-20180619/#svg-color)
  * `http`: HTTP or HTTPS URLs
  * `https`: HTTPS URLs
* Additional niche formats
  * `iban`: [IBAN (International Bank Account Number)](https://en.wikipedia.org/wiki/International_Bank_Account_Number)
  * `de_blz`: [German Bankleitzahl (BLZ)](https://de.wikipedia.org/wiki/Bankleitzahl)

## Planned features

* [ ] Allow generating an end user-friendly representation of a given schema, specifically to document available configuration options with title, description, default, example, etc.
* [ ] Add "type-casting" capability for formats that have a python-native type equivalent but are not part provided by JSON itself (e.g. convert `date` format properties to `datetime.date`, or `uuid` to `uuid.UUID`, etc.)
* [ ] Add more common formats and build a comprehensive library of possible formats (I'm planning on accepting PRs or issues for new formats regularly after reaching structural maturity for the project)

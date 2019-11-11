# Hass MAX! Cube integration with valve position support

Modified version of the [official Home Assistant MAX! Cube integration](https://www.home-assistant.io/integrations/maxcube).
Configuration works just the same as described in the documentation for the official integration.

## Installation

1. Download the files in this repository.
2. Put the files in `<home_assistant_config>/custom_components/maxcube`.
3. Add the `maxcube` configuration to your Home Assistant configuration if you never used the official component before.
4. Restart Home Assistant.

The valve position for each thermostat will be available in a new sensor with entity id `sensor.<name_of_thermostat>_valve_position`.

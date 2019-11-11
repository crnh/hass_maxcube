"""support for MAX! Thermostat valve position via MAX! cube"""
import logging

from homeassistant.helpers.entity import Entity

from . import DATA_KEY

_LOGGER = logging.getLogger(__name__)

UNIT_OF_MEASUREMENT = "%"

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Iterate through all MAX! Devices and add thermostats."""
    devices = []
    for handler in hass.data[DATA_KEY].values():
        cube = handler.cube
        for device in cube.devices:
            name = "{} {} valve position".format(cube.room_by_id(device.room_id).name, device.name)

            if cube.is_thermostat(device):
                devices.append(MaxCubeValveSensor(handler, name, device.rf_address))

    if devices:
        add_entities(devices)

class MaxCubeValveSensor(Entity):
    """MAX! Cube valve position sensor."""

    def __init__(self, handler, name, rf_address):
        self._name = name
        self._rf_address = rf_address
        self._cubehandle = handler
        self._unit_of_measurement = UNIT_OF_MEASUREMENT
        self._state = None
    
    @property
    def should_poll(self):
        """Return the polling state."""
        return True

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    @property
    def state(self):
        """Return true if the binary sensor is on/open."""
        return self._state

    def update(self):
        """Get latest data from MAX! Cube."""
        self._cubehandle.update()
        device = self._cubehandle.cube.device_by_rf(self._rf_address)
        self._state = device.valve_position

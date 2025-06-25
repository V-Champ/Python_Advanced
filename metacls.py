import importlib
import os

RELAY_INTERFACES = {
    "Arduino": ("Arduino", "ArduinoRelay"),
    "USB": ("USB", "USBRelay"),
}


class RelayException(Exception):
    pass


class Relay(object):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @classmethod
    def __new__(cls, *args, **kwargs):
        interface = kwargs.pop("relay_type")
        if not interface:
            interface = os.getenv("RELAY_TYPE", "Arduino")
        # Import the correct usb interface
        try:
            (module_name, class_name) = RELAY_INTERFACES[interface]
        except KeyError:
            raise NotImplementedError(
                "Relay interface '{}' not supported".format(interface)
            )

        try:
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
        except Exception as e:
            raise ImportError(
                "Cannot import class {} from module {} "
                "for Relay interface '{}': {}".format(
                    class_name, module_name, interface, e
                )
            )
        return cls(**kwargs)

obj = Relay(relay_type='Arduino', port='com19')
print(type(obj))
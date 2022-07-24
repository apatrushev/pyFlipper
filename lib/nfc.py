from .threaded import Threaded
import re

class NFC(Threaded):
    def __init__(self, serial_wrapper) -> None:
        self._serial_wrapper = serial_wrapper
        super().__init__()

    def detect(self, callback, timeout=None):
        def _run():
            p = re.compile(
                "found:\s([A-Z|\-]+)\sUID\slength:\s(\d+),\sUID:([\w|\d]+)")
            try:
                result = re.search(p, self._serial_wrapper.send("nfc detect")).groups()
                return  {'type': result[0], 'lenght': result[1], 'UID': result[2]}
            except Exception:
                return None
        self.exec(func=_run, callback=callback, timeout=timeout)

    def emulate(self, callback, timeout=None):
        def _run():
            data = self._serial_wrapper.send("nfc detect")
            #TODO parse data
            return data
        self.exec(func=_run, callback=callback, timeout=timeout)

    def field(self, callback, timeout=10):
        def _run():
            data = self._serial_wrapper.send("nfc field")
            #TODO parse data
            return data
        self.exec(func=_run, callback=callback, timeout=timeout)


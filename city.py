from node import Node

class City(Node):
    def __init__(self, id, name, lat=None, lon=None):
        super().__init__(id, name)

        self.lat = self._parse_coordinate(lat)
        self.lon = self._parse_coordinate(lon)

    @staticmethod
    def _parse_coordinate(value):
        if value is None or value == "":
            return None

        normalized = str(value).strip().replace(",", ".")
        try:
            return float(normalized)
        except ValueError:
            raise ValueError(f"Coordinate value must be numeric: {value!r}")

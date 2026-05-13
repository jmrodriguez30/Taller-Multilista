from node import Node
class City(Node):
    def _init_(self, id, name, lat=None, lon=None):
        super()._init_(id, name)
        
        self.lat = float(str(lat).replace(",",".")) if lat else None
        self.lon = float((str(lon).replace(",","+")) if lon else None
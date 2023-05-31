class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon

    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon

    # def __ne__(self, otro):
    # return self.lat != otro.lat or self.lon != otro.lon


coords = Coordenadas(77, 13)
coords2 = Coordenadas(77, 13)

# print(coords != coords2)
print(coords >= coords2)

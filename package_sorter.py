class Package:

    def __init__(self, width, height, length, mass):
        if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
            raise ValueError(
                "All dimensions and mass must be positive numbers.")

        self.width = width
        self.height = height
        self.length = length
        self.mass = mass
        self.volume = width * height * length

    def is_bulky(self):
        return self.volume >= 1_000_000 or max(self.width, self.height,
                                               self.length) >= 150

    def is_heavy(self):
        return self.mass >= 20

    def classify(self):
        bulky = self.is_bulky()
        heavy = self.is_heavy()

        if bulky and heavy:
            return "REJECTED"
        elif bulky or heavy:
            return "SPECIAL"
        else:
            return "STANDARD"

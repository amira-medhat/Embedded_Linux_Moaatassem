class AVR_GPIO:

    def __init__(self, port, pin, direction):
        self._port = port
        self._pin = pin
        self._direction = direction

        try:
            if self._direction == "IN":
                self.set_input()
            elif self._direction == "OUT":
                self.set_output()
        except:
            raise ValueError("Invalid direction: choose 'INPUT' or 'OUTPUT'")

    def set_output(self):
        if self._port == "A":
            DDRA |= 1 << self._pin
        elif self._port == "B":
            DDRB |= 1 << self._pin
        elif self._port == "C":
            DDRC |= 1 << self._pin
        elif self._port == "D":
            DDRD |= 1 << self._pin
        else:
            raise ValueError("Invalid port: choose 'A' or 'B' or 'C' or 'D'")

    def set_input(self):
        if self._port == "A":
            DDRA &= ~(1 << self._pin)
        elif self._port == "B":
            DDRB &= ~(1 << self._pin)
        elif self._port == "C":
            DDRC &= ~(1 << self._pin)
        elif self._port == "D":
            DDRD &= ~(1 << self._pin)
        else:
            raise ValueError("Invalid port: choose 'A' or 'B' or 'C' or 'D'")


def main():
    my_pin = AVR_GPIO("B", 3, "IN")


if __name__ == "__main__":
    main()

"""Model for aircraft flights"""


class Flight:
    """A flight with passenger aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("invalid airline code in '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("invalid router number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self, seat):
        """Parse the seat

        Args:
            seat: A seat designator such as 12C, 34B

        Returns:
            A tuple having seat row and column
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate seat to passengers

        Args:
            seat: A seat designator such as 12C, 34B
            passenger: The passenger name

        Raises:
            ValueError is seat is not available.
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate passenger

        Args:
        from_seat: Current seat of passenger
        to_seat: new seat of passenger
        """
        current_row, current_letter = self._parse_seat(from_seat)
        new_row, new_letter = self._parse_seat(to_seat)

        if self._seating[current_row][current_letter] is None:
            raise ValueError("No passenger to move from seat {}".format(from_seat))
        if self._seating[new_row][new_letter] is not None:
            raise ValueError("seat {} already occupied".format(to_seat))

        self._seating[new_row][new_letter] = self._seating[current_row][current_letter]
        self._seating[current_row][current_letter] = None

    def num_seat_available(self):
        return sum(sum(1 for s in row.values() if s is None) for row in self._seating if row is not None)

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))

    def make_boarding_cards(self, card_printer):
        for passenger , seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

    def registration(self):
        return self._registration

class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1, 56), "ABCDEGHJK"


def make_flight():
    f = Flight("AB090" ,AirbusA319("G-EUPT"))
    f.allocate_seat("1A", "Deepika")
    f.allocate_seat("2A", "Manoj")
    f.allocate_seat("12A", "Akshaj")
    f.allocate_seat("12B", "Aariya")
    f.allocate_seat("21A", "Anubhav")
    f.allocate_seat("21B", "Shivani")

    g = Flight("AB090", Boeing777("B111"))
    g.allocate_seat("1A", "Deepika")
    g.allocate_seat("2A", "Manoj")
    g.allocate_seat("12A", "Akshaj")
    g.allocate_seat("12B", "Aariya")
    g.allocate_seat("21A", "Anubhav")
    g.allocate_seat("21B", "Shivani")
    return f, g

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name: {0}" \
             "| Flight: {2}" \
             "| Seat: {1}" \
             "| Aircraft: {3}" \
             "|".format(passenger, seat, flight_number, aircraft )
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + '-' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Frank", 20.00)
        self.room_1 = Room(1, 100.00, 5.00, 4)

    def test_guest_has_name(self):
        self.assertEqual("Frank", self.guest.name)

    def test_guest_has_wallet(self):
        self.assertEqual(20.00, self.guest.wallet)

    def test_customer_can_pay_entrance_fee(self):
        room = Room(1, 100, 5, 4)
        self.guest.pay_entrance_fee(room)
        self.assertEqual(15.00, self.guest.wallet)

    def test_sufficient_funds__true_if_enough(self):
        self.assertEqual(True, self.guest.sufficient_funds(self.room_1))

    def test_sufficient_funds__false_if_not_enough(self):
        poor_guest = Guest("Neo", 0)
        self.assertEqual(False, poor_guest.sufficient_funds(self.room_1))

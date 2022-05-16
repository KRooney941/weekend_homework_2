import unittest
from src.song import Song
from src.guest import Guest
from src.room import Room


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room(1, 100.00, 5.00, 4)
        self.room_2 = Room(2, 100.00, 5.00, 4)

        self.guest = Guest("Frank", 20.00)
        self.guest_2 = Guest("Ted", 10.00)
        self.guest_3 = Guest("Sarah", 50.00)
        self.guest_4 = Guest("Kieran", 30.00)
        self.guest_5 = Guest("Cheeky", 20.00)

        self.song = Song("My Way", "Frank Sinatra")

    def test_room_has_no(self):
        self.assertEqual(1, self.room_1.room_no)

    def test_room_has_till(self):
        self.assertEqual(100.00, self.room_1.till)

    def test_room_has_entry_fee(self):
        self.assertEqual(5.00, self.room_1.entry_fee)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room_1.capacity)

    def test_guest_in_room_starts_at_0(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_add_guest_to_room(self):
        self.room_1.add_to_room(self.guest)
        self.assertEqual(1, self.room_1.guest_count())

    def test_guest_in_room_2_starts_at_0(self):
        self.assertEqual(0, self.room_1.guest_count())

    def test_add_guest_to_room_2(self):
        self.room_1.add_to_room(self.guest)
        self.assertEqual(1, self.room_1.guest_count())

    def test_remove_guest_from_room(self):
        self.room_1.add_to_room(self.guest)
        self.room_1.remove_from_room(self.guest)
        self.assertEqual(0, self.room_1.guest_count())

    def test_clear_room(self):
        self.room_1.add_to_room(self.guest)
        self.room_1.clear_list()
        self.assertEqual(0, self.room_1.guest_count())

    def test_song_list_starts_at_0(self):
        self.assertEqual(0, self.room_1.song_count())

    def test_add_song_to_list(self):
        self.room_1.add_song_to_list(self.song)
        self.assertEqual(1, self.room_1.song_count())

    def test_remove_song_from_room(self):
        self.room_1.add_song_to_list(self.song)
        self.room_1.remove_from_song_list(self.song)
        self.assertEqual(0, self.room_1.song_count())

    def test_clear_song_list(self):
        self.room_1.add_song_to_list(self.guest)
        self.room_1.clear_song_list()
        self.assertEqual(0, self.room_1.song_count())

    def test_check_capacity_works_with_less_than(self):
        self.room_1.add_to_room(self.guest)
        self.assertEqual(True, self.room_1.check_capacity())

    def test_max_capacity(self):
        self.room_2.add_to_room(self.guest)
        self.room_2.add_to_room(self.guest_2)
        self.room_2.add_to_room(self.guest_3)
        self.room_2.add_to_room(self.guest_4)
        self.room_2.add_to_room(self.guest_5)
        self.assertEqual(False, self.room_2.check_capacity())

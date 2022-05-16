class Room:

    def __init__(self, room_no, till, entry_fee, capacity):
        self.room_no = room_no
        self.till = till
        self.entry_fee = entry_fee
        self.capacity = capacity
        self.guests = []
        self.songs = []

    def guest_count(self):
        return len(self.guests)

    def check_capacity(self):
        if len(self.guests) < self.capacity:
            return True
        else:
            return False

    def add_to_room(self, guest):
        self.guests.append(guest)

    def remove_from_room(self, guest):
        self.guests.remove(guest)

    def clear_list(self):
        self.guests.clear()

    def song_count(self):
        return len(self.songs)

    def add_song_to_list(self, song):
        self.songs.append(song)

    def remove_from_song_list(self, song):
        self.songs.remove(song)

    def clear_song_list(self):
        self.songs.clear()

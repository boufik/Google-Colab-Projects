class Band:

    # 0. Constructor
    def __init__(self, name, origin, start_date, end_date, genres, members_names, members_instruments, albums_names, albums_dates):

        # 0a. Basic attributes
        self.name = name
        self.origin = origin
        self.start_date = start_date
        self.end_date = end_date
        self.genres = genres
        self.members_names = members_names
        self.members_instruments = members_instruments
        self.albums_names = albums_names
        self.albums_dates = albums_dates

        # 0b. Extra attributes
        self.years_active = f"{self.start_date} - {self.end_date} ({self.end_date - self.start_date} years active)"
        self.top_genre = self.genres[0]

        # 0c. String attributes
        self.members_all = []
        L1 = len(self.members_names)
        L2 = len(self.members_instruments)
        if L1 == L2:
            for i in range(L1):
                value = f"{self.members_names[i]} ({self.members_instruments[i]})"
                self.members_all.append(value)

        self.albums_all = []
        L3 = len(self.albums_names)
        L4 = len(self.albums_dates)
        if L3 == L4:
            for i in range(L3):
                value = f"{self.albums_names[i]} ({self.albums_dates[i]})"
                self.albums_all.append(value)

        self.most_famous_member = self.members_all[0]
        self.most_successful_album = self.albums_all[0]

        # 0d. Dictionary Attributes
        self.members = {}
        albums = {}
        if L1 == L2:
            self.members = {members_names[i] : members_instruments[i] for i in range(L1)}
        if L3 == L4:
            albums = {albums_dates[i] : albums_names[i] for i in range(L3)}

        # 0e. Sort the albums dictionary (by key = date)
        keys = list(albums.keys())
        keys = sorted(keys)
        self.albums = {key : albums[key] for key in keys}


    # Methods
    def show_all(self):
        print("\n\n-------- Band's Info --------\n")
        print(f"  Name: {self.name}")
        print(f"Origin: {self.origin}")
        print(f" Years: {self.years_active}\n")

        print("Genres:")
        for genre in self.genres:
            print(f"* {genre}")
        print(f"Top genre: {self.top_genre}\n")

        print("Members:")
        for key, value in self.members.items():
            print(f"* {key} ({value})")
        print(f"Most famous member: {self.most_famous_member}\n")

        print("Albums")
        for date, name in self.albums.items():
            print(f"* {name} ({date})")
        print(f"Most successful album: {self.most_successful_album}\n")

    def show_basics(self):
        print("\n\n-------- Band's Basic Info --------\n")
        print(f"  Name: {self.name}")
        print(f"Origin: {self.origin}")
        print(f" Years: {self.years_active}")
        print(f"Genres: {self.genres}\n")
        print(f"   Most famous member: {self.most_famous_member}")
        print(f"Most successful album: {self.most_successful_album}")



from datetime import date
today = date.today()
year_now = today.year

name1 = "Queen"
origin1 = "London, England"
start_date1 = 1970
end_date1 = year_now
genres1 = ["Rock", "Glam Rock", "Hard Rock", "Progressive Rock", "Psychedelic Rock", "Punk Rock", "Pop", "Heavy Metal", "RnB", "Funk and Disco"]
members_names1 = ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"]
members_instruments1 = ["Vocals, piano, keyboard", "Guitar, vocals, keyboard", "Drums, vocals", "Bass, guitar, backing vocal"]
albums_names1 = ["Queen", "A Night at the Opera", "Queen II", "Innuendo", "Made in Heaven", "A Kind of Magic", "News of the world", "Jazz", "The Game", "The Works", "Hot Space"]
albums_dates1 = [1973, 1975, 1974, 1991, 1995, 1986, 1977, 1978, 1980, 1984, 1982]

name2 = "Guns N' Roses"
origin2 = "Los Angeles, California, USA"
start_date2 = 1985
end_date2 = year_now
genres2 = ["Hard Rock", "Heavy Metal", "Classic Rock", "Classic Metal"]
members_names2 = ["Axl Rose", "Slash", "Duff McKagan", "Richard Fortus", "Dizzy Reed", "Frank Ferrer", "Melissa Reese"]
members_instruments2 = ["Vocals, Piano", "Guitar, backing vocals", "Bass, backing vocals", "Guitar, backing vocals", "Keyboard, piano", "Drums, backing vocals", "Synthesizer, keyboard, backing vocals, programming"]
albums_names2 = ["Appetite for Destruction", "Use your Illusion I", "Use your Illusion II", "Chinese Democracy", "Appetite for Democracy", "Nothing Lasts Forever", "Bad Obsession"]
albums_dates2 = [1987, 1991, 1991, 2008, 2014, 2021, 2019]

Queen = Band(name1, origin1, start_date1, end_date1, genres, members_names1, members_instruments1, albums_names1, albums_dates1)
Queen.show_all()
GNR = Band(name2, origin2, start_date2, end_date2, genres2, members_names2, members_instruments2, albums_names2, albums_dates2)
GNR.show_all()

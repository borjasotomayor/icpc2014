# Borja Sotomayor, 2014
#
# This python module defines a "hotels" variable with a list
# of ICPC hotels, and "distances" dictionary where the keys
# are all possible pairs of hotels, plus a (hotel, ICPC venue) pair.
#
# Note: I make some (hopefully fair) assumptions about the distances
#       between hotels. Suggestions, corrections, etc. are welcome.
#
# Feel free to reuse in other solutions for the #QuestBusRoutes quest.


# List of ICPC hotels
hotels = ["Hyatt Regency", "Green Park Hotel", "Ramada", "Atrium Palace Hotel", 
          "Park Inn", "Onegin", "Panorama", "Novotel"]

# These are the driving distances (in kilometers)
# reported by Google Maps
distances = { ("Hyatt Regency", "Green Park Hotel") : 2.8,
              ("Hyatt Regency", "Ramada") : 17.3,
              ("Hyatt Regency", "Atrium Palace Hotel") : 2.8,
              ("Hyatt Regency", "Park Inn") : 2.3,
              ("Hyatt Regency", "Onegin") : 2.6,
              ("Hyatt Regency", "Panorama") : 2.8,
              ("Hyatt Regency", "Novotel") : 2.3,
              ("Green Park Hotel", "Ramada") : 15.8,
              ("Green Park Hotel", "Atrium Palace Hotel") : 1.6,
              ("Green Park Hotel", "Park Inn") : 3.5,
              ("Green Park Hotel", "Onegin") : 3.0,
              ("Green Park Hotel", "Panorama") : 1.6,
              ("Green Park Hotel", "Novotel") : 2.0,
              ("Ramada", "Atrium Palace Hotel") : 9.6,
              ("Ramada", "Park Inn") : 11.5,
              ("Ramada", "Onegin") : 10.6,
              ("Ramada", "Panorama") : 9.6,
              ("Ramada", "Novotel") : 10.3,
              ("Atrium Palace Hotel", "Park Inn") : 2.1,
              ("Atrium Palace Hotel", "Onegin") : 1.2,
              ("Atrium Palace Hotel", "Panorama") : 0.013,
              ("Atrium Palace Hotel", "Novotel") : 0.85,
              ("Park Inn", "Onegin") : 1.3,
              ("Park Inn", "Panorama") : 1.5,
              ("Park Inn", "Novotel") : 0.95,
              ("Onegin", "Panorama") : 0.2,
              ("Onegin", "Novotel") : 0.85,
              ("Panorama", "Novotel") : 0.8,
            }

# We assume that the inverse paths have the same distance
for a,b in distances.keys():
    distances[(b,a)] = distances[(a,b)]

# ... except for the Ramada, where the inverse path
# is actually substantially different because of the highway
# exit you take in each direction.
distances[("Ramada", "Green Park Hotel")] = 10.3
distances[("Ramada", "Hyatt Regency")] = 12.3

distances[("Atrium Palace Hotel", "Ramada")] = 15.3
distances[("Park Inn", "Ramada")] = 16.9
distances[("Onegin", "Ramada")] = 15.3
distances[("Panorama", "Ramada")] = 15.3
distances[("Novotel", "Ramada")] = 15.8




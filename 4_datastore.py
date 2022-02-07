# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.'


"""
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

"""


datastore = {
    "medical": [  # Datastore only has one key, medical. Medical has a list of keys, which are dictionaries.
        {"room-number": 100, "use": "reception", "sq-ft": 50, "price": 75},
        {"room-number": 101, "use": "waiting", "sq-ft": 250, "price": 75},
        {"room-number": 102, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 103, "use": "examination", "sq-ft": 125, "price": 150},
        {"room-number": 104, "use": "office", "sq-ft": 150, "price": 100},
    ]
}

# Answer is below
outfile = open("retail_space.csv", "w")
outfile.write("room-number,use,sq-ft,price\n")
# Write a for loop here
mylist = datastore[
    "medical"
]  # When you give a dictionary a key, it gives you the values. Since the value
# of the key "medical" is a list of dictionaries, it gives us that.
print(type(mylist))

for l in mylist:  # l represents each dictionary in mylist
    outfile.write(
        str(
            l["room-number"]
        )  # You HAVE to convert to string before you write to a file.
        + ","
        + l[
            "use"
        ]  # you don't need a string function here because all of the uses are already strings
        + ","
        + str(l["sq-ft"])
        + ","
        + str(l["price"])
        + "\n"
    )
# If something is a list, you need to give it an index value. If it's a dictionary, you need to give it a key.


# for l in datastore["medical"]:
#    print(type(l))  # This tells us that l is a dictionary

outfile.close()

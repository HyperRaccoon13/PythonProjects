import json

particleJSON = "python falling sand V2/particles.json"
particlesList = []

def LoadPariclesFromJSON(path, particlesList):
# Open the JSON file and load the data
    try:
        with open(path) as f:
            data = json.load(f)
        print("Successfully loaded JSON data.")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")

    # Iterate over each particle set in the data
    for particleData in data:
        name = particleData['name']
        properties = particleData['properties']

        # Create a dictionary to store particle properties
        particleDict = {
            'name': name,
            'group': properties['group'],
            "speed": properties["speed"],
            'colour': properties['colour'],
            'affectByGravity': properties['affectByGravity'],
            'mass': properties['mass'],
            'flammable': properties['flammable']
        }

        # Append the dictionary to the particles_list
        particlesList.append(particleDict)

    # Print the list of particle properties
    
    return particlesList

for particle in LoadPariclesFromJSON(particleJSON, particlesList):
    print( particle)
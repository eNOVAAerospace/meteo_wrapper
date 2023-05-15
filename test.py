def read_parameters(file_name):
    with open(file_name, "r") as file:
        parameters = {}
        for line in file:
            key, value = line.strip().split(":")
            parameters[key.strip()] = value.strip()
    country = parameters.get("country")
    start_date = parameters.get("start date")
    end_date = parameters.get("end date")

    return country, start_date, end_date


# Appel de la fonction et récupération des valeurs
country, start_date, end_date = read_parameters("parameter.txt")

# Affichage des valeurs
print("Country:", country)
print("Start Date:", start_date)
print("End Date:", end_date)

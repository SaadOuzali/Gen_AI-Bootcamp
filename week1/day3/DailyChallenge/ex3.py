brand_info_dict = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": ["Amancio", "Ortega", "Gaona"],
    "type_of_clothes": ["men", "woman", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]},
}


brand_info_dict["number_stores"]=2

brand_info_dict["country_creation"]="spain"

new_competitor="Desigual"
if "international_competitors" in brand_info_dict:
    brand_info_dict["international_competitors"].append(new_competitor)
   

del brand_info_dict["creation_date"]


major_us_color = brand_info_dict["major_color"]["US"]
print(f"the major US color is : {major_us_color}")
print(brand_info_dict["international_competitors"][-1])
print(f"number of keys in brand dict : {len(brand_info_dict)}")
print(f"all the keys of brand dict : {brand_info_dict.keys()}")


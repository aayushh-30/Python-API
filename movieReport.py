import requests

def getData(name):
    base_url = "https://www.omdbapi.com/?apikey="
    api_key = "ENTER YOUR API KEY"
    complete_base_url = f"{base_url}{api_key}&s={name}" 
    response = requests.get(complete_base_url)
    data = response.json()

    if data.get("Response") == "True" and "Search" in data:
        lists = data["Search"]
        myDict = {}
        for item in lists: 
            myDict[item["Title"]] = item["Year"]
        
        return myDict
    else:
        return "Unable to Find the Movie"

def main():
    try:
        movie_name = input("Enter Movie Name: ")
        data = getData(movie_name)
        for key,value in data.items():
            print(f"Title: {key}, Year: {value}")
    except Exception as e:
        print("An error occurred: " + str(e))

if __name__ == "__main__":  
    main()

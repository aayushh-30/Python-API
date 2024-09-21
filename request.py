import requests

def fetching_docs_of_url():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        country_name = user_data["location"]["country"]

        return user_name,country_name
    else:
        raise Exception("Failes to fetch user Data")

def main():
    try:
        name,country = fetching_docs_of_url()
        print(f"Username : {name}\n Country : {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
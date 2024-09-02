import requests


def main():
    token = ""
    url = "https://api.github.com/repos/falkoin/ptymer/pulls"
    params= {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github.raw+json", "X-GitHub-Api-Version": "2022-11-28"}

    response = requests.get(url=url, params=params)
    print("Response:")
    print(response)
    data = response.json()

    print(data)


if __name__ == "__main__":
    main()

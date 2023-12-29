import requests
from bs4 import BeautifulSoup

url = "https://australia.national-lottery.com/saturday-lotto/results-archive-2023"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    ul_elements = soup.find_all("ul", class_="balls")

    results_list = []

    for ul_element in ul_elements:
        li_elements = ul_element.find_all("li", class_="result medium saturday-lotto ball dark ball")

        numbers = [int(li.text.strip()) for li in li_elements]
        results_list.append(numbers)

    print(results_list)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

import requests
from bs4 import BeautifulSoup

URL = "https://abcnews.go.com/Elections/2020-us-presidential-election-results-live-map"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="BalanceOfPowerContainer")

election_elems = results.find_all("div",  class_="BalanceOfPower")

print("According to ABC News")
print("----------------------------------------\n")

for election_elem in election_elems:
    candidate_elem = election_elem.find_all("div", class_="Candidate__Name")
    electoral_elem = election_elem.find_all("div", class_="Candidate__Votes")
    vote_elem = election_elem.find_all('div', class_='PopVote')
    if None in (candidate_elem, electoral_elem):
        continue
    for i in range(2):
        print(candidate_elem[i].text.strip() + " - " + electoral_elem[i].text.strip() + "/270 Electoral Votes")
        print(vote_elem[i].text.strip()[:-6] + " Total Votes")
        print()

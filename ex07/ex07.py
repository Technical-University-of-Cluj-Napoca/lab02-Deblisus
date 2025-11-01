import requests
from bs4 import BeautifulSoup

job = "python"

URL = f"https://www.juniors.ro/jobs?q={job}"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

jobs = soup.find_all("li", class_="job")

for job in jobs:
    title = " ".join(job.find("h3").text.split())
    company = job.find("ul", class_="job_requirements")
    company = " ".join(company.find("li").text.split()[1:])
    location = " ".join(job.find("div", class_="job_header_title").find("strong").text.split("\n")[1].split())
    tags = job.find("ul", class_="job_tags")
    tags = tags.find_all("li")
    tags = ", ".join([x.text for x in tags])
    post_date = " ".join(job.find("div", class_="job_header_title").find("strong").text.split("\n")[2].split())[2:]
    print(title)
    print(company)
    print(location)
    print(tags)
    print(post_date)
    break
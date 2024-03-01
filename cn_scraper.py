from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("https://wearecodenation.com/2024/01/23/data-course-playground/").text
soup = BeautifulSoup(html_text, "lxml")

h5s = soup.find_all("h5", class_="elementor-heading-title elementor-size-default")

course_dates = {}

for h5Tag in h5s:
    if ":" in h5Tag.text:
        course_dates[h5Tag.text] = []
        dates = h5Tag.find_next("h6")
        for single_date in dates.strings:
            course_dates[h5Tag.text].append(single_date)

print(course_dates)

##ACTIVITY 2

updated_dates = { key: pd.Series(value) for key, value in course_dates.items() }

df = pd.DataFrame(updated_dates)

print(df)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import csv
import os
import time


chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Open the webpage
driver = webdriver.Chrome(service_args=["--executable-path=chromedriver.exe"])
transcript_links = [
    "https://www.rev.com/transcript-editor/shared/8a5sVeujVA22gdi12p-UUAb4SqJmdBHjtZ0Td9CIm0rqx_bi_lwBwYaHAvfI7rRIjs73IbvQ_6j_bI4yT_1fEhbenl4?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/OYOdTRzd3LdT25OWLK8Alx7P94p6fo5gGQyPn_Szg1cmgSkx69_SPGpcfMUizIGREQJmS2wpbAYHJFagHyPZ1ZT0vak?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/5yM_GR7amPkL8-AVlIPhOz5fzHX5Cxn5kTrcUUYJ0AiQEhe0lIn9S82DdKMtHVNHuOEWs-lvxPeLYeqZgFQzoIB2lRA?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/ZX2vskwsraQAphAMilqnT_KGx4tOA3ugqRxHt2DHYlez0u_LvFnm1yy9eC2Oen4W3tAtEdFhBGIXjNT3qSO22Sg6R_0?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/5EJ4zLlSlIiYGUJZUhaNpsdZO5MYWPB7EDNOGpqy285af3xOa_NxiFIzXRZ4yyEUFtzrms3dOmb32DBF6re3cdwCrLM?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/DUh0yxQrSCe1h8M6DbfoxgifIh7y5kTFCWIOpwKHw3-UN9GlFTHIsrH7ElmLASUkfbB2hN4V5r85XfStBpLjezojzdg?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/LFyxypEiTTBuIAyjFAcaWGuYp_r_nAKCn25oIk5Yw2TMFyuFSti-QGMYufsJHTTtikRgTAtTAqhKGZ7WZDSS5EzRHbA?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/cxOLinkkGcCDH9RsvdZbXCjYSK75nxHFQ6Vm943bQ071YfYqIKFzzI0SRNLzElaM-MRAmgL8kfJMD85ipGjnnQi0E-M?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/mbUpirO0gXxX6bZcydh1AvVLzpXCgUtJaYr5LJ3DzuQbXYbGuLo7qOg8ikBN-aJjNmxkxgs1rQfRmLpQmjgG-PkWUmQ?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/m5dXMEQlKWvJQfrmdt4nC6Nja96ehXQ_lV8cVbD-H1bs2rFhApSAHX3menJdoRU7DW7vj5YTGbrXGToCsDJHd1LR9_g?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/Q1Sn9OfwC5VX1Hqt57rGd4vwEDdizpnsmPKMHSHzqHGC3R2h9p2IzZ7ZdtOKncmdgsX3gYA--xMnDHtdn60bBb-8Mt8?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/B2n73dhe-_ckb6etxclWPsh8hlGW6Uz84Q1G6zlBESj4e9S_jyKWzbY_UlJy3anIh6CS-kGTADv4T_92yCz8maa9CCQ?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/DBU6ivOavG0ylubrdmuXrpjGFF2Yxx_wGYrfDWuVC3FsYOD16EZGpxo9qPce36R-7ptm7lBx28BiGgkLlevFm1EM2yA?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/kvKusHedC0cbww3d5oP2uNSLt4vcBqHMAgXdOz-K1ej1u8j-_yfiKob8KRJKOsoVAMT3GATJAZJKZ1PytOjsoUdSEk0?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/9xdvb8zsrhHCAX_hnsgqJtDXvdCaT2Y6JIbL4w5GPpYlL0Yqfiddg066IWhhdFYY_lKa28U9_q5kSfCUvIv7SjAieGI?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/mWWoMtcWDt0x0h00rwY37yahxhKz1IYwXefeESOnyx3pYicRplI4u2wDZJT_ptp1N36FdMyrGmO19dFE9GQTDZtOCAc?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/u7SxS3erz5csC6YBgfS99AnJRN8L0QpCnHEkcOjQ-QlO9hfdg7tu8dc9mZuR5AjVvBEm7D9xoiz5Xk8fylzZ93R03g4?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/6deSthU_ZnhnO9qy3cRVt9MMDHTczUUL-OOxOmyXpZ5__bsg_tK7uey05iW9dJ-qyf5gX2VayvzCk-stgD5YsN7T_jI?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/l02J9Y-6cY59F_nIR_yYxJDxQk5UUkL7vtGxAic4J5diQcZtlu8TLxdbOxE98HjqE6FAHpyfRNqA3HpvdFFY5O18_cM?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/7RAeNYu3lK6X3NGh0gI_gmkSnZO7vxE2eX_O78s40yonExtOdeqK6ASbzApPxjparRcWg8dB1cn_ghe0pP1iQMgbmJs?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/UtmmdrX2dWacs0nXOH2SksmC68A_lVWpOIDB9nG6HLa_neyBbuNCKfu_tNNIb4OgZlk5SsUK0jJaBHi6Ki4YC3j3OQY?loadFrom=SharedLink",
    "https://www.rev.com/transcript-editor/shared/LLYv9Yu-bTlHRCnwJdrQMl_MHRsoIthRvy2U_h1SCIVIfJheftm80cFYkXeXSQ1picAAKGFfbX22v-AASIrgs60txtc?loadFrom=SharedLink",
]

# create list of data to be written to the CSV file
data = [["transcript_link", "transcript_text"]]

for transcript_link in transcript_links:
    driver.get(transcript_link)

    # Wait 5 seconds
    driver.implicitly_wait(7)

    # Scrape text content of element #editor
    try:
        element = driver.find_element(By.ID, "editor")
        transcript_text = element.text
    except:
        transcript_text = "no transcript text found"

    # Append to list item with value of transcript_link and value of transcript_text variables to data variable list
    data.append([transcript_link, transcript_text])

    time.sleep(4)

# file name of the CSV file to be deleted
file_name = "example.csv"

# delete the CSV file if it exists
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"{file_name} was deleted.")
else:
    print(f"{file_name} does not exist.")


# create the CSV file and write the data to it
with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

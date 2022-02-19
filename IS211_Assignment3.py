import argparse
import urllib.request
import datetime
import csv
import re


def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        web_data = response.read().decode('utf-8')

    return web_data


def main(url):
    """
    Main function
    :param url:
    :return:
    """
    print(f"Running main with URL = {url}...")
    # Read the url into a big string
    data = downloadData(url)
    # split big string file into lines
    data_lines = data.split("\n")
    # Use csv module to split the lines into components before processing
    browser_count = {
        'FIREFOX': 0,
        'CHROME': 0,
        'MSIE': 0,
        'SAFARI': 0
    }
    image_counter = 0

    for row in csv.reader(data_lines):
        # Skip empty lines
        if len(row) == 0:
            continue
        # url_hit = row[0]
        # timestamp = row[1]

        url_hit, timestamp_str, browser, _, hit_size = row
        # find images...
        url_hit = url_hit.upper()
        if re.search("PNG|GIF|JPG", url_hit.upper()):
            image_counter += 1


        # count browsers
        if browser.upper().find("FIREFOX") != -1:
            browser_count['FIREFOX'] += 1
        elif browser.upper().find("MSIE") != -1:
            browser_count['MSIE'] += 1
        elif browser.upper().find("CHROME") != -1:
            browser_count['CHROME'] += 1
        elif browser.upper().find("SAFARI") != -1:
            browser_count['SAFARI'] += 1


            print('hour {} has {} hits'.format(timestamp.hour, image_counter)) #extra credit


        image_hits = (int(image_counter) / int(10000))
        percentage_hits = "{:.0%}".format(image_hits)

        max_browser = max(browser_count, key=browser_count.get)  # get key with max value.
        # print(max_browser)


        timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")


    print("images account for {} of all requests".format(percentage_hits))
    #print(image_counter)
    #print(browser_count)
    print ("the most popular browser is {}".format(max_browser))












if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)







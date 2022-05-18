"""
Bradley Kimutai Kosgei
CS51A
Assignment 12
04/25/2022

"""
from stackqueue import *
from urllib import error
from urllib.request import urlopen
import time
import ssl


def is_valid_pomona_url(url):
    """
    A boolean to check for pomona.edu websites
    :param url: (str) a URL
    :return: (bool) True or False
    """
    return "pomona.edu" in url and " " not in url


def is_full_url(url):
    """
    A boolean to check whether a URL is a full website address
    :param url: (str) a URL
    :return: (bool) True or False
    """
    if "http" == url[:4]:  # checks for the first 5 positions of the string not including the fifth
        return True
    return False


def get_all_urls(url):
    """
     Get the URLs available from the course web page and
    return them in a list
    :param url: (str) a URL
    :return: (list) weblinks on the given page
    """
    try:
        web_page = urlopen(url)  # opens the URL
    except error.HTTPError:  # checks whether the page we are searching for exists
        print("Ignoring: " + url)
        return []

    except error.URLError:  # checks whether the server exists
        print("Ignoring: " + url)
        return []

    urls = []  # makes an empty list

    search_line = "<a href="  # checks for these words in the webpage

    for line in web_page:  # iterates through every line in the webpage
        line = line.decode('ISO-8859-1').strip()  # making a best guess using an encoding scheme

        if search_line in line:  # looks for the words in the lines of the webpage
            begin_index = line.find(search_line)  # in-built function find is used to find the words
            end_index = line.find('"', begin_index + 9)
            if is_full_url(line[begin_index + 9:end_index]):  # checks to see if it is a full url with
                # 'pomona.edu'
                urls.append(line[begin_index + 9:end_index])  # appends the webpages in to the list

    return urls


def filter_pomona_urls(list_of_urls):
    """
    Filters out the urls that do not have pomona.edu
    :param list_of_urls: (list) a list of urls
    :return: (list) a new list that are of pomona
    """
    new_lst = []  # creating a new list

    for url in list_of_urls:  # iterates over the urls in the list
        if is_valid_pomona_url(url):  # checks to see if it is a valid url
            new_lst.append(url)  # appends the valid urls into a list
    return new_lst


def crawl_pomona(url, to_visit, max_number):
    """
    Crawls through the Pomona webpages and returns a list of all the pomona.edu websites it can visit
    starting the crawl from the starting url
    :param url: (str) a url
    :param to_visit: Queue or Stack
    :param max_number: (int) th maximum number we can get to
    :return: (List) a list of visited urls
    """
    lst = to_visit
    lst.add(url)
    visited = []  # making an empty list for the visited urls
    visited_set = set()  # making an empty set

    while len(visited) < max_number:  # the function does not stop until we get to our maximum number
        if not lst.is_empty():  # checks if the to_visit list is empty
            removed = lst.remove()  # the removed url
            urls = filter_pomona_urls(get_all_urls(removed))

            if removed not in visited_set:  # checks to see if the removed url is in the visited list
                # only moves to the next step if it is not in the list
                for url in urls:  # iterates over the pomona.edu urls
                    lst.add(url)  # adds them to the to_visit list
                print("Crawling:" + removed)
                visited.append(removed)  # adds the removed url to te visited list
                visited_set.add(removed)  # adds the removed url to te visited set
                time.sleep(0.1)

            else:
                pass  # does nothing if removed is in the visited list or set
        else:
            break  # does nothing if the list is empty

    return visited


def write_pomona_urls(url, to_visit, max_number, output_file):
    """
    Writes the results of crawling into an output file
    :param url: (str) a url
    :param to_visit: Stack or Queue
    :param max_number: (int) the maximum number we can get to
    :param output_file: (str)a file
    :return: None
    """
    out = open(output_file, "w")  # gives a variable name to the file and opens it

    visited = crawl_pomona(url, to_visit, max_number)  # calls the previous function

    for item in visited:  # iterates over the visited list
        out.write(item + "\n")  # we write the urls into the file
    out.close()  # closes the file


"""
The stack which uses depth first search is slower and goes through one thing till it gets to the very end
like, for example, mine goes into the economics major and goes deeper into faculty members. The queue is
much faster as it goes over just the 'main' weblinks and thus avoids going deeper into unnecessary stuff. 
It would be better to use the queue over 100 URLs as it is faster and goes over important links and gives a 
variety instead of going deeper into a specific link and give us links we do not need and most of them might 
have errors
"""





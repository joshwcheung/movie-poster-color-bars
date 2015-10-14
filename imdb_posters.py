#!/usr/bin/python
from imdbpie import Imdb
import color_clustering as cc
import argparse
import cv2
import os
import re
import unicodedata
import urllib

def make_output_dirs(k):
    """Creates output directories if they do not exist.

    Args:
        k: The number of clusters.
    """
    if not os.path.exists('posters'):
        os.makedirs('posters')
    if not os.path.exists('quantized_posters_' + str(k)):
        os.makedirs('quantized_posters_' + str(k))
    if not os.path.exists('color_bars_' + str(k)):
        os.makedirs('color_bars_' + str(k))

def slug(str):
    """Formats a string to a valid filename.

    Removes special unicode characters and symbols from the string. Replaces 
    whitespace with underscores.

    Args:
        str: The input string.
    Returns:
        output: The formatted string.
    """
    output = unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
    output = unicode(re.sub('[^\w\s-]', '', output).strip().lower())
    output = unicode(re.sub('[-\s]+', '_', output))
    return output

def write_posters(movies):
    """Saves movie poster images from an IMDb movie list.

    Using urls from each movie dictionary from the movie list, writes png files 
    of each movie poster. A filename consists of the movie title, prefixed by 
    its IMDb rank. Movie poster images are written to the directory 'posters'.

    Args:
        movies: A list of movies containing a dictionary for each movie. The 
        list is sorted by IMDb rank.
    """
    rank = 1
    for movie in movies:
        filename = str(rank) + '_' + slug(movie['title']) + '.png'
        urllib.urlretrieve(movie['image']['url'], 'posters/' + filename)
        rank += 1

def process_poster(poster, k):
    """Produces a color quantized poster and a color bar from a poster.

    Uses k-means clustering to produce a color quantized version of a poster. 
    Then, draws a color bar from the color quantized poster. The color 
    quantized poster is written to the directory 'quantized_posters_k'; the 
    color bar is written to the directory 'color_bars_k'.

    Args:
        poster: The filename of the movie poster stored in 'poster'.
        k: The number of clusters.
    """
    #Read image and perform k-means clustering
    img = cv2.imread(poster)
    clustered, labels, centers = cc.kmeans_color_quant(img, k)

    #Get density histogram and draw color bar from histogram
    hist = cc.get_histogram(labels)
    bar = cc.draw_color_bar(hist, centers)

    #Write color quantized poster and color bar
    quantname = os.path.basename(os.path.splitext(poster)[0]) + '_quant.png'
    barname = os.path.basename(os.path.splitext(poster)[0]) + '_bar.png'
    cv2.imwrite('quantized_posters_' + str(k) + '/' + quantname, clustered)
    cv2.imwrite('color_bars_' + str(k) + '/' + barname, bar)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--clusters', required=True, type=int, 
                        help='Number of cluters')
    args = vars(parser.parse_args())

    k = args['clusters']
    make_output_dirs(k)

    if os.listdir('posters') == []:
        imdb = Imdb(anonymize=True)
        top = imdb.top_250()
        write_posters(top)
    
    qp_dir = 'quantized_posters_' + str(k) + '/'
    cb_dir = 'color_bars_' + str(k) + '/'
    if (os.listdir(qp_dir) == []) and (os.listdir(cb_dir) == []):
        posters = os.listdir('posters')
        for poster in posters:
            process_poster('posters/' + poster, k)

if __name__ == '__main__':
    main()

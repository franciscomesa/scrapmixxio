# Mixx.io sources (scrapping Mixx.io)

This project is just to work/test web scrapping. Also, generate stats.

Process:
1. Analyze source, website mixx.io.
2. Scrape HTML content.
    * Home.
    * Other pages.
3. Parse HTML with Beautiful Soup.
4. Build job search tool.
5. Additional work.

Product:
1. List of links used.
2. List of sites and density.
3. Some statistics.
    - Length text
    - Number of links 

## Analyze source
Mixx.io is a usable website, easy to use in phones. Structure from the links perspective:
* Home: links to latests podcasts, pagination and other pages.
* Posts: audio and links used in podcast. Also sponsor link.
* Pagination: Each page have about 30 links to posts.
* Other pages.


## Future features
- Length podcast episode
- Audio analysis


---
`TODO`

## Scrape HTML content

### Remove sponsor links
Now (2020-08-25) sponsors, are under the first `blockquote` tag. In general all the notes are under this HTML tag.




## Parse HTML with Beautiful Soup


## Build job search tool


## Additional work
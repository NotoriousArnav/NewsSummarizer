#Documentation for the API
Base URL: /api/v1/

### Endpoints: 
 - /
 - /available_articles
 - /get_article/{base64 encoded url link}

## /
Hitting the enpoint, will show available sources for news articles

## /available_articles
Hitting this endpoint will result to show available articles from the sources.
The list updates every 2 minutes

## /get_article/{base64 encoded url link}
Hitting this endpoint with a valid base64 encoded url link, will result in showing the deatils about the article, and the sumary of the article.
Only Returnsa valid response if the url is valid or is supported by the scrappe
Hitting this endpoint with a valid base64 encoded url link, will result in showing the deatils about the article, and the sumary of the article.
Only Returnsa valid response if the url is valid or is supported by the scrapper

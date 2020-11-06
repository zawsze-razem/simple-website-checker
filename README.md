# Simple Website Checker
An extremely minimalistic website availability checker.

Sends a request over both http and https to the provided URL and outputs very basic information based on the response.

Currently it show its status code, searches for the Server header, and more specific headers based on response codes:
- Calculates content length for 2XX reponses
- Searches for the location heading for 4XX responses

Why would anyone use it? ¯\\\_(ツ)\_/¯

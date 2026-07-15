There is an access log in the working directory named "environmet/access.log". 
Analyze the traffic and summarize what you find — how many requests there were, the clients involved, and which pages
were popular - save in a file named "report.json". 
Save your findings so they can be reviewed.

The JSON object must contain exactly these fields:
{
  "total_requests": <integer>,
  "unique_ips": <integer>,
  "top_path": "<string>"
}
Definitions:
- total_requests = total number of log entries
- unique_ips = number of unique client IP addresses
- top_path = request path with the largest number of requests

Do not print the JSON to stdout. Save it to `report.json`.

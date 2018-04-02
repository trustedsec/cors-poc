# cors-poc
Companion code for TrustedSec's "CORS Findings: Another Way to Comprehend"
  blog post. See https://www.trustedsec.com/2018/04/cors-findings/ to understand situations where this could be useful.
## Usage
* `git clone https://github.com/trustedsec/cors-poc`
* `cd cors-poc`
* Edit **corstest.html** to update [target-site/target-page] and [our-server].
* `python3 -m http.server --cgi` **Caution:** all files in the current directory and sub-directories will be served on 
   HTTP port 8000.
* Browse to **corstest.html** from a "victim" browser.

If all goes well, cross-origin responses from the victim browser will be displayed and also stored in **captured-post-data.txt**.


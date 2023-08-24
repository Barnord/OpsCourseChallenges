#!/bin/bash

# let it be known the skipped challenges were a batch file and some powershell. Powershell is worthwhile, but those challenges seemed for for familiarizing oneself with it, which isn't useful to me at this juncture. Also batch isn't worth focusing on if I'm comfortable with bash. I'm not, but still.

printf "Please enter a domain name sans the www\n"
read domain

printf "\nwhois $domain\n"
whois $domain
printf "\ndig $domain\n"
dig $domain
printf "\nhost $domain\n"
host $domain
printf "\nnslookup $domain\n"
nslookup $domain

#changed all echos to printf for access to the newline escape character, however apparently printf behaves more consistently across different environments than echo does anyway. Which is good since after a little continued reading I can just add an -e flag to echo for the same result.
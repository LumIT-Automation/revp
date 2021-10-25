%postun
#!/bin/bash

printf "\n* Container postrm...\n"

# $1 is the number of time that this package is present on the system. If this script is run from an upgrade and not
if [ "$1" -eq "0" ]; then
    if podman volume ls | awk '{print $2}' | grep -Eq ^revp$; then
        printf "\n* Clean up revp volume...\n"
        podman volume rm revp
    fi
fi

exit 0

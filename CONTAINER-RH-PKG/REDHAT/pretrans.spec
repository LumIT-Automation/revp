%pretrans
#!/bin/bash

printf "\n* Container prerm...\n"
printf "\n* Cleanup...\n" 

if getenforce | grep -q Enforcing;then
    echo -e "\nWarning: \e[32mselinux enabled\e[0m. Stop the installation process.\n"
    exit 1
fi

exit 0


%post
#!/bin/bash

printf "\n* Container postinst...\n" | tee -a /dev/tty

printf "\n* Building podman image...\n" | tee -a /dev/tty
cd /usr/lib/revp

# Build container image.
buildah bud -t revp . | tee -a /dev/tty

printf "\n* The container will start in few seconds.\n\n"

function containerSetup()
{
    cd /usr/lib/revp

    # First container run: associate name, bind ports, bind fs volume, define init process, ...
    podman run -p 80:80/tcp -p 443:443/tcp --name revp -v revp:/etc/nginx/tls -dt localhost/revp /sbin/init # bind port to HOST.

    printf "\n* Starting Container Service...\n"
    systemctl daemon-reload

    systemctl start automation-interface-revp-container # (upon installation, container is already run).
    systemctl enable automation-interface-revp-container
}

systemctl start atd

{ declare -f; cat << EOM; } | at now
containerSetup
EOM

exit 0


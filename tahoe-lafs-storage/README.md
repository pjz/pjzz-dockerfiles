# Tahoe-LAFS Storage Node

To build:

    docker build --rm -t tahoe-storage
    
To run:

    # path to persisted tahoe storage - will be bind-mounted into the container
    STORAGE=/tahoe
    # host port to map to the storage's listening port
    PORT=58273

    # command to start the node
    #  * the internal port (34567) and internal mountpoint (/tahoe) are hardcoded in the image,
    #    so changing them will make the node not work correctly

    docker run -v $STORAGE:/tahoe -p $PORT:34567 -i -t tahoe-storage <nickname> <introducer-url>


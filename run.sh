# !bin/bash

echo "OPENFACE CONNECTION"

docker start openface
docker exec -it openface /bin/bash run_server.sh

echo "OPENFACE 



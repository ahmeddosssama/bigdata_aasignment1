$CONTAINER_NAME = "gracious_hofstadter"
$OUTPUT_DIRECTORY = ".\service-result"

# Ensure the output directory exists
New-Item -Path $OUTPUT_DIRECTORY -ItemType Directory -Force | Out-Null

# Copy files from the Docker container to the output directory
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/res_dpre.csv $OUTPUT_DIRECTORY\res_dpre.csv
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-1.txt $OUTPUT_DIRECTORY\eda-in-1.txt
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-2.txt $OUTPUT_DIRECTORY\eda-in-2.txt
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-3.txt $OUTPUT_DIRECTORY\eda-in-3.txt
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/vis.png $OUTPUT_DIRECTORY\vis.png
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/k.txt $OUTPUT_DIRECTORY\k.txt

# Stop the Docker container
docker stop $CONTAINER_NAME

# Output message
Write-Host "Output files copied and container stopped."

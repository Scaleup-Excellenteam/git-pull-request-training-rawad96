NUM_FILES=${1:-50}
DATE=$(date +"%Y-%m-%d")
DIR_NAME="zero_${DATE}_files"

mkdir "$DIR_NAME"

for i in $(seq 1 $NUM_FILES)
do
    FILE_NAME="File_${i}.dat"
    head -c 1024 < /dev/zero > "$DIR_NAME/$FILE_NAME"
done

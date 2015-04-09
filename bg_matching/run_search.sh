CODE_PATH=/home/rgirdhar/data/Work/Code/0002_Retrieval/ScalableLSH/DiskE2LSH
$CODE_PATH/main.bin \
    -k 500 \
    -d /memexdata/Dataset/processed/0001_Backpage/Features/CNN/pool5_normed \
    -n /memexdata/Dataset/processed/0001_Backpage/Images/lists/temp/Images_50K.txt \
    -l /memexdata/Dataset/processed/0001_Backpage/Search/indexes/fullImg_225bit.index \
    -o /memexdata/Dataset/processed/0001_Backpage/Search/results/temp/res_fullImg \
    -m /memexdata/Dataset/processed/0001_Backpage/Search/results/temp/query.txt

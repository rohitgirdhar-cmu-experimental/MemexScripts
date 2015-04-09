CODE_PATH=/home/rgirdhar/data/Work/Code/0002_Retrieval/ScalableLSH/DiskE2LSH
$CODE_PATH/main.bin \
    -k 50 \
    -d /memexdata/Dataset/processed/0001_Backpage/Features/CNN/pool5_bg_normed \
    -n /memexdata/Dataset/processed/0001_Backpage/Images/lists/Images.txt \
    -l /memexdata/Dataset/processed/0001_Backpage/Search/indexes/temp/bgImg_1-5M_225bit.index \
    -o /memexdata/Dataset/processed/0001_Backpage/Search/results/temp/res \
    -m /memexdata/Dataset/processed/0001_Backpage/Search/results/temp/query.txt

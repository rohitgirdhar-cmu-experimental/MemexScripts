CODE_PATH=/home/rgirdhar/data/Work/Code/0002_Retrieval/ScalableLSH/DiskE2LSH
$CODE_PATH/buildIndex.bin \
    -d /home/rgirdhar/memexdata/Dataset/processed/0001_Backpage/Features/CNN/pool5_bg_normed \
    -n /home/rgirdhar/memexdata/Dataset/processed/0001_Backpage/Images/lists/temp/Images_1-5M.txt \
    -s /home/rgirdhar/memexdata/Dataset/processed/0001_Backpage/Search/indexes/temp/bgImg_1-5M_225bit.index \
    -b 225 \
    -t 15 \
    -a 1800

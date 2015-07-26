CODE_PATH=/home/rgirdhar/data/Work/Code/0002_Retrieval/Try/ScalableLSH/DiskE2LSH/storage/tools/
nice -n 10 $CODE_PATH/compressStore.bin \
       -i ~/memexdata/Dataset/processed/0006_BackpageExtended/Features/CNN/pool5_normed/ \
       -o ~/memexdata/Dataset/processed/0002_BackpageComplete/Features/CNN/pool5_normed_compressed/ \
       -k /home/rgirdhar/memexdata/Dataset/processed/0002_BackpageComplete/Images/lists/feature_ids.txt \
       -s 268932

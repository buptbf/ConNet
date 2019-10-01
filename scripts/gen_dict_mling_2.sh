export CUDA_DEVICE_ORDER=PCI_BUS_ID
green=`tput setaf 2`
reset=`tput sgr0`

echo ${green}=== Generating Dictionary ===${reset}

TRAIN_DATA="/home/molly_data/ouyu/data/panx_dataset/raw_data"
DEV_DATA="/home/molly_data/ouyu/data/panx_dataset/raw_data"
TEST_DATA="/home/molly_data/ouyu/data/panx_dataset/raw_data"
EMBEDDING_DATA="/home/molly_data/ouyu/data/panx_dataset/word_emb/muse/"
OUTPUT_DATA="/home/molly_data/ouyu/data/panx_dataset/raw_data"
LANGS="af ar bg bn bs ca cs da de el en es et fa fi fr he hi hr hu id it lt lv mk ms nl no pl pt ro ru sk sl sq sv ta tl tr uk vi"

for LANG in da de el en es et #fa fi fr he hi hr hu id it lt lv mk ms nl no pl pt ro ru sk sl sq sv ta tl tr uk vi
do
  python pre_seq/gene_map_mling.py --train_corpus_path $TRAIN_DATA --input_embedding_path $EMBEDDING_DATA --output_path $OUTPUT_DATA --lang $LANG
done

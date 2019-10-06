# ConNet

This project is for ``Learning to Contextually Aggregate Multi-Source Supervision for Sequence Labeling".

## Dependency

Our package is based on Python 3.6 and the following packages:
```
numpy
tqdm
torch-scope
torch==0.4.1
```

## Crowd-Sourcing

* Generate the word dictionary by:
```
python pre_seq/gene_map.py -h
```

* Encode the dictionary by:
```
python pre_seq/encode_data.py -h
```

* Train/Test the decoupling phase by:
```
python train_seq_decoupling.py -h
python test_seq_decoupling.py -h
```

* Train/Test the aggregation phase by:
```
python train_seq_aggregation.py -h
python test_seq_aggregation.py -h
```

## Cross-Domain



## Citation

[Efficient Contextualized Representation: Language Model Pruning for Sequence Labeling](https://arxiv.org/abs/1804.07827)
```
@inproceedings{liu2018efficient,
  title = "{Efficient Contextualized Representation: Language Model Pruning for Sequence Labeling}", 
  author = {Liu, Liyuan and Ren, Xiang and Shang, Jingbo and Peng, Jian and Han, Jiawei}, 
  booktitle = {EMNLP}, 
  year = 2018, 
}
```
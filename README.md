# NP_wrap

NP_wrap is a wrapper for analyzing the quality of fastq.gz files. it will loop over a folder containing your fastq.gz files and put all normal NanoPlot output in a corresponding output folder. this way you can allways find back which information belongs to which barcode. Besides this, NP_wrap also provides you with a DataFrame.tsv file which holds all information of the given barcodes in one table. This makes comparison of quality between barcodes easier.

## create an environment to install nanoplot

```
conda create -n NP
```
```
conda activate NP
```

now install the needed script 
```
git clone https://github.com/daanbrackel/NP_wrap
```

move into the NP_wrap directory:
```
cd NP_wrap
```
now we can run the help function of the script:
```
python NP_total.py -h
```
as the input you can give it a folder containing all fastq.gz files. the output can be any directory desired by the user. for instance:

`python NP_total.py ../data_storage/2324-043_SUP/ ../Nanoplot_result/2324-043_SUP/`

you can also add an alias so you can run the script from every location:
```
echo "alias NP='your/path/to/NP_wrap/NP_total.py'"  >> ~/.bashrc
```
```
source ~/.bashrc
```
```
NP "path to inputfolder" "path to outputfolder"
```

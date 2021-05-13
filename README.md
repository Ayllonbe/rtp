# RTP 

RTP is a project grated with 100 000 kr from KSLA and 20 000 kr from SPPS. The main goal was to merge two knowledge, gene networks inferred by gene expression data and link annotations from protein-protein interaction networks, and then using machine learning to learn if is there any pattern between the inferred gene network and the known links to annotate unknown gene links. 

The projet is unfinished, since it requires to run `Submit_aab_rtp.sh`. The main issue why I could not run it was the issues with the HPC server that has not installed conda. In the `README.md` file into `scripts/ToServerAnalysis` you will have the necessary instruction how to run it to have the TPOT in your HPC (if you installed conda).

Previous work (not shown here), present a interesting result for *binding* and *reaction* connection when using **random forest** approaches. For that reason, to be sure of that, we decided to use TPOT, a auto Machine Learning library that uses genetic algorithm to find the Machine Learning approach that optimize the best the prediction. A first try (not shown here) provide a high performance with **extra trees** and **random forest** in *Arabidopsis thaliana*. This github projet is ready to run an analysis for six organisms: *Arabidopsis thaliana* (athal), *Populus tremula* (potra), *Eucalyptus grandis* (eugra), *Saccharomyces cerevisiae* (scere), and *Drosophila melanogaster* (dmel). The data preparation is explained in `doc` folder.

The full projet should include the following tree. The data are remove in github since it uses many storage.

**Note**: Since the TPOT will use the organisms independently, I did preprocessing special for the organism. That means, that some organism will includes more columns than others. You should consider that when run the analysis to compare the different organisms, since TPOT is to observe if the predictor consensus for all organisms is related to **random forest**.

```
.
├── LICENSE
├── README.md
├── data
│   └── rtp_project_data
│       ├── README.md
│       ├── athal-network.txt
│       ├── athal.protein.actions.v11.0.txt.gz
│       ├── dmel-network.txt
│       ├── dmel.protein.actions.v11.0.txt
│       ├── eugra-network.txt
│       ├── eugraV2.protein.actions.v11.0.txt
│       ├── eugra_network.tsv
│       ├── potra-network.txt
│       ├── potra.protein.actions.v11.0.txt
│       ├── scere-network.txt
│       └── scere.protein.actions.v11.0.txt.gz
├── doc
│   ├── full-analysis.html
│   ├── preprocesingData.athal.txt
│   ├── preprocesingData.dmel.txt
│   ├── preprocesingData.eugra.txt
│   ├── preprocesingData.potra.txt
│   └── preprocesingData.scere.txt
└── scripts
    ├── ToServerAnalysis
    │   ├── DataToRunTPOT
    │   │   ├── athal_binding_to_SK1.pkl
    │   │   ├── athal_binding_to_SK10.pkl
    │   │   ├── athal_binding_to_SK2.pkl
    │   │   ├── athal_binding_to_SK3.pkl
    │   │   ├── athal_binding_to_SK4.pkl
    │   │   ├── athal_binding_to_SK5.pkl
    │   │   ├── athal_binding_to_SK6.pkl
    │   │   ├── athal_binding_to_SK7.pkl
    │   │   ├── athal_binding_to_SK8.pkl
    │   │   ├── athal_binding_to_SK9.pkl
    │   │   ├── athal_catalysis_to_SK1.pkl
    │   │   ├── athal_catalysis_to_SK10.pkl
    │   │   ├── athal_catalysis_to_SK2.pkl
    │   │   ├── athal_catalysis_to_SK3.pkl
    │   │   ├── athal_catalysis_to_SK4.pkl
    │   │   ├── athal_catalysis_to_SK5.pkl
    │   │   ├── athal_catalysis_to_SK6.pkl
    │   │   ├── athal_catalysis_to_SK7.pkl
    │   │   ├── athal_catalysis_to_SK8.pkl
    │   │   ├── athal_catalysis_to_SK9.pkl
    │   │   ├── athal_reaction_to_SK1.pkl
    │   │   ├── athal_reaction_to_SK10.pkl
    │   │   ├── athal_reaction_to_SK2.pkl
    │   │   ├── athal_reaction_to_SK3.pkl
    │   │   ├── athal_reaction_to_SK4.pkl
    │   │   ├── athal_reaction_to_SK5.pkl
    │   │   ├── athal_reaction_to_SK6.pkl
    │   │   ├── athal_reaction_to_SK7.pkl
    │   │   ├── athal_reaction_to_SK8.pkl
    │   │   ├── athal_reaction_to_SK9.pkl
    │   │   ├── athal_regulation_to_SK1.pkl
    │   │   ├── athal_regulation_to_SK10.pkl
    │   │   ├── athal_regulation_to_SK2.pkl
    │   │   ├── athal_regulation_to_SK3.pkl
    │   │   ├── athal_regulation_to_SK4.pkl
    │   │   ├── athal_regulation_to_SK5.pkl
    │   │   ├── athal_regulation_to_SK6.pkl
    │   │   ├── athal_regulation_to_SK7.pkl
    │   │   ├── athal_regulation_to_SK8.pkl
    │   │   ├── athal_regulation_to_SK9.pkl
    │   │   ├── dmel_binding_to_SK1.pkl
    │   │   ├── dmel_binding_to_SK10.pkl
    │   │   ├── dmel_binding_to_SK2.pkl
    │   │   ├── dmel_binding_to_SK3.pkl
    │   │   ├── dmel_binding_to_SK4.pkl
    │   │   ├── dmel_binding_to_SK5.pkl
    │   │   ├── dmel_binding_to_SK6.pkl
    │   │   ├── dmel_binding_to_SK7.pkl
    │   │   ├── dmel_binding_to_SK8.pkl
    │   │   ├── dmel_binding_to_SK9.pkl
    │   │   ├── dmel_catalysis_to_SK1.pkl
    │   │   ├── dmel_catalysis_to_SK10.pkl
    │   │   ├── dmel_catalysis_to_SK2.pkl
    │   │   ├── dmel_catalysis_to_SK3.pkl
    │   │   ├── dmel_catalysis_to_SK4.pkl
    │   │   ├── dmel_catalysis_to_SK5.pkl
    │   │   ├── dmel_catalysis_to_SK6.pkl
    │   │   ├── dmel_catalysis_to_SK7.pkl
    │   │   ├── dmel_catalysis_to_SK8.pkl
    │   │   ├── dmel_catalysis_to_SK9.pkl
    │   │   ├── dmel_reaction_to_SK1.pkl
    │   │   ├── dmel_reaction_to_SK10.pkl
    │   │   ├── dmel_reaction_to_SK2.pkl
    │   │   ├── dmel_reaction_to_SK3.pkl
    │   │   ├── dmel_reaction_to_SK4.pkl
    │   │   ├── dmel_reaction_to_SK5.pkl
    │   │   ├── dmel_reaction_to_SK6.pkl
    │   │   ├── dmel_reaction_to_SK7.pkl
    │   │   ├── dmel_reaction_to_SK8.pkl
    │   │   ├── dmel_reaction_to_SK9.pkl
    │   │   ├── dmel_regulation_to_SK1.pkl
    │   │   ├── dmel_regulation_to_SK10.pkl
    │   │   ├── dmel_regulation_to_SK2.pkl
    │   │   ├── dmel_regulation_to_SK3.pkl
    │   │   ├── dmel_regulation_to_SK4.pkl
    │   │   ├── dmel_regulation_to_SK5.pkl
    │   │   ├── dmel_regulation_to_SK6.pkl
    │   │   ├── dmel_regulation_to_SK7.pkl
    │   │   ├── dmel_regulation_to_SK8.pkl
    │   │   ├── dmel_regulation_to_SK9.pkl
    │   │   ├── eugra_binding_to_SK1.pkl
    │   │   ├── eugra_binding_to_SK10.pkl
    │   │   ├── eugra_binding_to_SK2.pkl
    │   │   ├── eugra_binding_to_SK3.pkl
    │   │   ├── eugra_binding_to_SK4.pkl
    │   │   ├── eugra_binding_to_SK5.pkl
    │   │   ├── eugra_binding_to_SK6.pkl
    │   │   ├── eugra_binding_to_SK7.pkl
    │   │   ├── eugra_binding_to_SK8.pkl
    │   │   ├── eugra_binding_to_SK9.pkl
    │   │   ├── eugra_catalysis_to_SK1.pkl
    │   │   ├── eugra_catalysis_to_SK10.pkl
    │   │   ├── eugra_catalysis_to_SK2.pkl
    │   │   ├── eugra_catalysis_to_SK3.pkl
    │   │   ├── eugra_catalysis_to_SK4.pkl
    │   │   ├── eugra_catalysis_to_SK5.pkl
    │   │   ├── eugra_catalysis_to_SK6.pkl
    │   │   ├── eugra_catalysis_to_SK7.pkl
    │   │   ├── eugra_catalysis_to_SK8.pkl
    │   │   ├── eugra_catalysis_to_SK9.pkl
    │   │   ├── eugra_reaction_to_SK1.pkl
    │   │   ├── eugra_reaction_to_SK10.pkl
    │   │   ├── eugra_reaction_to_SK2.pkl
    │   │   ├── eugra_reaction_to_SK3.pkl
    │   │   ├── eugra_reaction_to_SK4.pkl
    │   │   ├── eugra_reaction_to_SK5.pkl
    │   │   ├── eugra_reaction_to_SK6.pkl
    │   │   ├── eugra_reaction_to_SK7.pkl
    │   │   ├── eugra_reaction_to_SK8.pkl
    │   │   ├── eugra_reaction_to_SK9.pkl
    │   │   ├── eugra_regulation_to_SK1.pkl
    │   │   ├── eugra_regulation_to_SK10.pkl
    │   │   ├── eugra_regulation_to_SK2.pkl
    │   │   ├── eugra_regulation_to_SK3.pkl
    │   │   ├── eugra_regulation_to_SK4.pkl
    │   │   ├── eugra_regulation_to_SK5.pkl
    │   │   ├── eugra_regulation_to_SK6.pkl
    │   │   ├── eugra_regulation_to_SK7.pkl
    │   │   ├── eugra_regulation_to_SK8.pkl
    │   │   ├── eugra_regulation_to_SK9.pkl
    │   │   ├── potra_binding_to_SK1.pkl
    │   │   ├── potra_binding_to_SK10.pkl
    │   │   ├── potra_binding_to_SK2.pkl
    │   │   ├── potra_binding_to_SK3.pkl
    │   │   ├── potra_binding_to_SK4.pkl
    │   │   ├── potra_binding_to_SK5.pkl
    │   │   ├── potra_binding_to_SK6.pkl
    │   │   ├── potra_binding_to_SK7.pkl
    │   │   ├── potra_binding_to_SK8.pkl
    │   │   ├── potra_binding_to_SK9.pkl
    │   │   ├── potra_catalysis_to_SK1.pkl
    │   │   ├── potra_catalysis_to_SK10.pkl
    │   │   ├── potra_catalysis_to_SK2.pkl
    │   │   ├── potra_catalysis_to_SK3.pkl
    │   │   ├── potra_catalysis_to_SK4.pkl
    │   │   ├── potra_catalysis_to_SK5.pkl
    │   │   ├── potra_catalysis_to_SK6.pkl
    │   │   ├── potra_catalysis_to_SK7.pkl
    │   │   ├── potra_catalysis_to_SK8.pkl
    │   │   ├── potra_catalysis_to_SK9.pkl
    │   │   ├── potra_reaction_to_SK1.pkl
    │   │   ├── potra_reaction_to_SK10.pkl
    │   │   ├── potra_reaction_to_SK2.pkl
    │   │   ├── potra_reaction_to_SK3.pkl
    │   │   ├── potra_reaction_to_SK4.pkl
    │   │   ├── potra_reaction_to_SK5.pkl
    │   │   ├── potra_reaction_to_SK6.pkl
    │   │   ├── potra_reaction_to_SK7.pkl
    │   │   ├── potra_reaction_to_SK8.pkl
    │   │   ├── potra_reaction_to_SK9.pkl
    │   │   ├── potra_regulation_to_SK1.pkl
    │   │   ├── potra_regulation_to_SK10.pkl
    │   │   ├── potra_regulation_to_SK2.pkl
    │   │   ├── potra_regulation_to_SK3.pkl
    │   │   ├── potra_regulation_to_SK4.pkl
    │   │   ├── potra_regulation_to_SK5.pkl
    │   │   ├── potra_regulation_to_SK6.pkl
    │   │   ├── potra_regulation_to_SK7.pkl
    │   │   ├── potra_regulation_to_SK8.pkl
    │   │   ├── potra_regulation_to_SK9.pkl
    │   │   ├── scere_binding_to_SK1.pkl
    │   │   ├── scere_binding_to_SK10.pkl
    │   │   ├── scere_binding_to_SK2.pkl
    │   │   ├── scere_binding_to_SK3.pkl
    │   │   ├── scere_binding_to_SK4.pkl
    │   │   ├── scere_binding_to_SK5.pkl
    │   │   ├── scere_binding_to_SK6.pkl
    │   │   ├── scere_binding_to_SK7.pkl
    │   │   ├── scere_binding_to_SK8.pkl
    │   │   ├── scere_binding_to_SK9.pkl
    │   │   ├── scere_catalysis_to_SK1.pkl
    │   │   ├── scere_catalysis_to_SK10.pkl
    │   │   ├── scere_catalysis_to_SK2.pkl
    │   │   ├── scere_catalysis_to_SK3.pkl
    │   │   ├── scere_catalysis_to_SK4.pkl
    │   │   ├── scere_catalysis_to_SK5.pkl
    │   │   ├── scere_catalysis_to_SK6.pkl
    │   │   ├── scere_catalysis_to_SK7.pkl
    │   │   ├── scere_catalysis_to_SK8.pkl
    │   │   ├── scere_catalysis_to_SK9.pkl
    │   │   ├── scere_reaction_to_SK1.pkl
    │   │   ├── scere_reaction_to_SK10.pkl
    │   │   ├── scere_reaction_to_SK2.pkl
    │   │   ├── scere_reaction_to_SK3.pkl
    │   │   ├── scere_reaction_to_SK4.pkl
    │   │   ├── scere_reaction_to_SK5.pkl
    │   │   ├── scere_reaction_to_SK6.pkl
    │   │   ├── scere_reaction_to_SK7.pkl
    │   │   ├── scere_reaction_to_SK8.pkl
    │   │   ├── scere_reaction_to_SK9.pkl
    │   │   ├── scere_regulation_to_SK1.pkl
    │   │   ├── scere_regulation_to_SK10.pkl
    │   │   ├── scere_regulation_to_SK2.pkl
    │   │   ├── scere_regulation_to_SK3.pkl
    │   │   ├── scere_regulation_to_SK4.pkl
    │   │   ├── scere_regulation_to_SK5.pkl
    │   │   ├── scere_regulation_to_SK6.pkl
    │   │   ├── scere_regulation_to_SK7.pkl
    │   │   ├── scere_regulation_to_SK8.pkl
    │   │   └── scere_regulation_to_SK9.pkl
    │   ├── README.md
    │   ├── Submit_aab_rtp.sh
    │   ├── aab_rtp.sh
    │   ├── analysisTPOT.py
    │   ├── env.yaml
    │   ├── prepareCVSKF.py
    │   ├── preprocessing.py
    │   ├── requirements.txt
    │   ├── results
    │   │   ├── athal.processed_data.tsv
    │   │   ├── dmel.processed_data.tsv
    │   │   ├── eugra.processed_data.tsv
    │   │   ├── potra.processed_data.tsv
    │   │   └── scere.processed_data.tsv
    │   └── test.py
    ├── athal-preprocessing.py
    ├── dmel-preprocessing.py
    ├── eugra-preprocessing.py
    ├── full-analysis.ipynb
    ├── potra-preprocessing.py
    └── scere-preprocessing.py
```
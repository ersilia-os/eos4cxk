# SARS-CoV-2 Anti viral screening

ImageMol is a Representation Learning Framework that utilizes molecule images for encoding molecular inputs as machine readable vectors for downstream tasks such as bio-activity prediction, drug metabolism analysis, or drug toxicity prediction. The approach utilizes transfer learning, that is, pre-training the model on massive unlabeled datasets to help it in generalizing feature extraction and then fine tuning on specific tasks. This model is fine tuned on 13 assays concerned with a number of target categories ranging from viral entry to toxicity in humans. These interactions are formulated as binary classification tasks

This model was incorporated on 2023-01-25.

## Information
### Identifiers
- **Ersilia Identifier:** `eos4cxk`
- **Slug:** `image-mol-sars-cov2`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `COVID-19`
- **Target Organism:** `SARS-CoV-2`
- **Tags:** `Sars-CoV-2`, `Antiviral activity`, `COVID19`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `13`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of the molecule being active in each assay

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| 3cl | float | high | probability of inhibiting the 3CL protease |
| ace2 | float | high | probability of inhibiting the ACE2 enzyme |
| alphalisa | float | high | probability of inhibiting the spike-ace2 interaction |
| cov2_cpe | float | high | probability of cytopathic effect |
| cov2_cytotox | float | high | probability of cytotoxicity as counterscreen for cov2-cpe |
| cov_ppe | float | high | probability of inhibiting the viral entrance with CoV1 pseudoparticles |
| cov_ppe_cs | float | high | counterscreen for the cov_ppe |
| hek293 | float | high | probability of cytotoxicity in hek293 cells |
| human | float | high | probability of cytotoxicity in human fibroblasts |
| mers_ppe | float | high | probability of inhibiting the viral entrance in MERS pseudoparticles |

_10 of 13 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos4cxk](https://hub.docker.com/r/ersiliaos/eos4cxk)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4cxk.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos4cxk.zip)

### Resource Consumption


### References
- **Source Code**: [https://github.com/HongxinXiang/ImageMol](https://github.com/HongxinXiang/ImageMol)
- **Publication**: [https://www.nature.com/articles/s42256-022-00557-6](https://www.nature.com/articles/s42256-022-00557-6)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [DhanshreeA](https://github.com/DhanshreeA)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos4cxk
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos4cxk
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!

# SARS-CoV-2 Anti viral screening

ImageMol is a Representation Learning Framework that utilizes molecule images for encoding molecular inputs as machine readable vectors for downstream tasks such as bio-activity prediction, drug metabolism analysis, or drug toxicity prediction. The approach utilizes transfer learning, that is, pre-training the model on massive unlabeled datasets to help it in generalizing feature extraction and then fine tuning on specific tasks. This model is fine tuned on 13 assays concerned with a number of target categories ranging from viral entry to toxicity in humans. These interactions are formulated as binary classification tasks

## Identifiers

* EOS model ID: `eos4cxk`
* Slug: `sars-cov-2-antiviral-screen`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Boolean`
* Output Type: `Integer`
* Output Shape: `List`
* Interpretation: The output is comprised of binary classification across thirteen assays that are as follows: 3C-like enzymatic activity (3CL), ACE2 enzymatic activity (ACE2), Human Embryonic Kidney 293 Cell line toxicity (HEK293), Human fibroblast toxicity (Human), MERS Pseudotyped particle entry (MERS_PPE), MERS Pseudotyped particle entry counterscreen (MERS_PPE_cs), SarsCov Pseudotyped particle entry (Cov_PPE), SarsCov Pseudotyped particle entry counterscreen (Cov_PPE_cs), SarsCov2 cytopathic effect (COV2_CPE), SarsCov2 cytopathic effect counterscreen (COV2_Cytotox), Spike ACE2 Protein-protein interaction (AlphaLISA), Spike ACE2 Protein-protein interaction counterscreen (TruHit), Transmembrane protease serine 2 enzymatic activity (TMPRSS2)

## References

* [Publication](https://www.nature.com/articles/s42256-022-00557-6)
* [Source Code](https://github.com/HongxinXiang/ImageMol)
* Ersilia contributor: [DhanshreeA](https://github.com/DhanshreeA)

## Citation

If you use this model, please cite the [original authors](https://www.nature.com/articles/s42256-022-00557-6) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!
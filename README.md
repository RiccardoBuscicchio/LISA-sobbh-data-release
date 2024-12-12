# LISA-sobbh-data-release

Data release supporting:
_Stellar-mass black-hole binaries in LISA: characteristics and complementarity with current-generation interferometers_

R.Buscicchio, J.Torrado, C.Caprini, G.Nardini, N.Karnesis, M.Pieroni, A.Sesana. 
[arXiv: 2410.18171](https://arxiv.org/abs/2410.18171).

## Credits

You are welcome to use this dataset in your research. We kindly ask you to cite the paper above.

If you want to cite specifically the data release, its DOI is: 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14384634.svg)](https://doi.org/10.5281/zenodo.14384634)

And the content is mapped in [github release page](https://github.com/RiccardoBuscicchio/LISA-sobbh-data-release/releases). 


## Data

Minimal data behind figures are provided within the repository in the `./data/` subfolder.

## Content

In `./notebooks`, we provide a jupyter notebook for the following figures:

- Figure 1: `./notebooks/Figure1.ipynb`
- Figure 2a: `./notebooks/Figure2a.ipynb`
- Figure 2b: `./notebooks/Figure2b.ipynb`
- Figure 4: `./notebooks/Figure4.ipynb`
- Figure 5: `./notebooks/Figure5.ipynb`
- Figure 8: `./notebooks/Figure8.ipynb`
- Figure 9: `./notebooks/Figure9.ipynb`

Figure 6, Figure 7, Figure 3 and Figure 10 require large datasets to be produced.
Feel free to get in touch with the authors, should you need access to the data.
 
## Requirements

Feel free to use `./sobbh.yaml` to create a conda environment to reproduce our figures, with 
```bash
conda env create -f sobbh.yaml
```

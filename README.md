# Zebrafish cleavage experiment

Custom Python and Fiji/ImageJ scripts used for image processing, analysis, quantification and data handling in:

> Tong, X., Li, Y. *et al.* Non-canonical cytokinesis is driven by nematic-flow-mediated mechanical uncoupling and adhesion-based invagination. *Nature Cell Biology* (2026). Accepted.

Code for the accompanying biophysical modelling is available separately at
[Irene-Li/Zebrafish_cleavage](https://github.com/Irene-Li/Zebrafish_cleavage).

## Requirements

The analysis scripts are built on NumPy, SciPy, scikit-image, scikit-learn, statsmodels, pandas, Matplotlib and Seaborn. Exact package versions are listed in the Methods section of the manuscript. Some steps additionally use Fiji/ImageJ (`.ijm` macros) and PIVLab in MATLAB, as noted below.

## Installation

Several notebooks import `xint_toolbox` (see below). Either place the `xint_toolbox` folder in your project directory, or install it into your conda environment:

```bash
conda activate <your-env>
pip install -e 0_xint_toolbox
```

## Repository structure

### `0_general` — general-purpose utilities

| Script | Description |
| --- | --- |
| `generate_LUT.ipynb` | Converts Matplotlib colormaps into LUTs for use in Fiji/ImageJ. |
| `generate_kymo.ipynb` | Generates kymographs in batch. |
| `get_embryo_position.ijm` | Reads image metadata and exports stage position coordinates (Fiji macro). |
| `get_the_date_modified.ipynb` | Extracts file modification times of image files. |
| `same_egg_identifier.ipynb` | Groups replicates belonging to the same embryo based on stage position coordinates. |
| `stretch_or_compress_to_balance_xy_pixel_size.ijm` | Rescales one axis so that pixel size and voxel depth match after reslicing in Fiji/ImageJ. |

### `0_xint_toolbox` — shared function library

A personal package by Xin Tong providing functions for data management, data visualization, mathematical operations, statistics and data processing, including nematic order calculation and particle image velocimetry.

### `1_embryo_surface_geometry`

Image processing, analysis and visualization of embryo surface geometry.
*Used for Fig. 1D, 1E, 2A and Extended Data Fig. 1C–1F, 2A, 2A′.*

| Notebook | Description |
| --- | --- |
| `1_1_embryo_surface_detection.ipynb` | Converts preprocessed z-stack time-lapse videos into height-map movies. |
| `1_2_embryo_cleavage_furrow_analysis.ipynb` | Extracts geometric measurements, including the curvature of the cleaving embryo and of the cleavage furrow, and plots the results. |
| `1_3_furrow_length_and_curvature_plot.ipynb` | Summarizes furrow length and curvature across replicates and plots them. |

### `2_furrow_indentation_and_membrane_invagination`

*Used for Fig. 1F′, 6D, 6E, 6F′, 6G′, 6H, 7C, 7D.*
 
| Notebook | Description |
| --- | --- |
| `2_1_furrow_indentation_and_membrane_invagination_analysis.ipynb` | Analyses cleavage furrow indentation, membrane septum invagination, furrow opening angles and cell cycle staging across conditions (wild type, Ca²⁺-free medium, CARhoA overexpression, IAA treatment, DMSO treatment). |

### `3_cortical_actin_and_myosin`

Quantification of actin and myosin fluorescence intensity, actin alignment and cortical flow behaviour.
*Used for Fig. 2F, 3E, 5B, 5D, 5D′, 5E and Extended Data Fig. 2B, 2C, 4B, 6B–6F, 6I, 7B.*

| Notebook | Description |
| --- | --- |
| `3_1_cortex_flow_analysis_general.ipynb` | Quantifies fluorescence intensity and nematic order from preprocessed high-magnification actin movies, computes flow divergence from PIV data exported by PIVLab (MATLAB), and plots the results. |
| `3_2_cortex_flow_analysis_compare_wt_and_carhoa.ipynb` | Compares actin alignment and flow behaviour between control embryos and embryos overexpressing CARhoA. |
| `3_3_actin_and_myosin_localization_analysis.ipynb` | Analyses the localization of actin and myosin in the cell cortex. |

### `4_laser_ablation`

Analysis of laser ablation experiments.
*Used for Fig. 4A′, 4B, 4B′, 4C, 5C and Extended Data Fig. 4A, 4A′, 5A, 5A′, 6G, 6H.*

| Notebook | Description |
| --- | --- |
| `4_1_calculate_nematic_order.ipynb` | Calculates the nematic order at the ablation site prior to ablation. |
| `4_2_calculate_recoiling_velocity.ipynb` | Calculates the initial recoil velocity after ablation from kymographs taken perpendicular to the cut. |
| `4_3_analyze_nematic_order_and_recoiling_velocity.ipynb` | Analyses nematic order and initial recoil velocity across developmental time, ablation positions and conditions, and plots the results. |
| `4_4_calculate_hydrodynamic_length.ipynb` | Fits the flow profile along the cleavage furrow after ablation to obtain the hydrodynamic screening length. |
| `4_5_analyze_huge_ablation.ipynb` | Plots flow profiles for embryos subjected to large ablations. |
| `4_6_analyze_double_ablation.ipynb` | Analyses the nematic order of the cable fragment between two ablations. |

## Citation

If you find this code useful, a citation to the paper is appreciated but not required.
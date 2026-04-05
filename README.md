# Region Captioning With SAM3, Florence-2, and BLIP-2

This repository focuses on an interactive region-captioning workflow:

1. segment an object or region with SAM3,
2. crop the detected region,
3. compare captions for the original image and the cropped region,
4. use both Florence-2 and BLIP-2 for side-by-side analysis.

The goal is to keep the original workflow intact while making the notebook runnable and easier to understand.

## Repository structure

```text
region-captioning-with-sam-florence-blip/
|-- assets/
|   |-- example_input.jpg
|   |-- sam_crop.jpg
|   |-- florence_output.jpg
|   `-- blip_output.jpg
|-- notebooks/
|   |-- code.ipynb
|   `-- region_captioning_demo.ipynb
|-- README.md
|-- requirements.txt
`-- .gitignore
```

## Notebook overview

- `notebooks/code.ipynb`: the main interactive notebook. It keeps the original project goal: SAM3-based segmentation, cropped-region analysis, automatic region labeling, and Florence-2 vs BLIP-2 comparison.
- `notebooks/region_captioning_demo.ipynb`: a smaller scripted demo version of the pipeline.

## Main workflow in `code.ipynb`

The interactive notebook lets you:

- upload an image or load one from a URL,
- segment with text prompts or box prompts,
- auto-label the selected region,
- save cropped outputs into `cropped_outputs/`,
- compare original-image and cropped-image captions,
- compare Florence-2 and BLIP-2 outputs side by side.

## Setup

Create and activate a Python environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

If you want GPU acceleration, install a CUDA-enabled PyTorch build before running the notebook.

## Run

For the full interactive workflow, open:

```bash
jupyter notebook notebooks/code.ipynb
```

For the smaller scripted example, open:

```bash
jupyter notebook notebooks/region_captioning_demo.ipynb
```

## Notes

- `code.ipynb` has been updated to keep the original goal while removing hardcoded local paths and fixing environment-specific issues.
- Florence-2 and BLIP-2 are loaded from your Hugging Face cache when available.
- Generated files such as `cropped_outputs/`, `outputs/`, and dataset downloads are ignored by Git.
- In environments without the interactive widget backend, the notebook falls back gracefully instead of crashing.

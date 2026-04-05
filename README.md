# Region Captioning With SAM, Florence-2, and BLIP

This repository is a small demo for a simple vision-language workflow:

1. detect a region with SAM3 from a text prompt,
2. crop the detected region,
3. caption that crop with Florence-2,
4. optionally caption the same crop with BLIP.

The project is intentionally minimal so the full pipeline is easy to read and reuse.

## Repository structure

```text
region-captioning-with-sam-florence-blip/
|-- assets/
|   |-- example_input.jpg
|   |-- sam_crop.jpg
|   |-- florence_output.jpg
|   `-- blip_output.jpg
|-- notebooks/
|   `-- region_captioning_demo.ipynb
|-- README.md
|-- requirements.txt
`-- .gitignore
```

## What each file contains

- `assets/example_input.jpg`: sample image used in the demo.
- `assets/sam_crop.jpg`: cropped region produced after segmentation.
- `assets/florence_output.jpg`: example Florence-2 output visualization.
- `assets/blip_output.jpg`: example BLIP-side result asset.
- `notebooks/region_captioning_demo.ipynb`: the main notebook for running the workflow end to end.

## Setup

Create and activate a Python environment, then install the dependencies:

```bash
pip install -r requirements.txt
```

If you want GPU acceleration, install a CUDA-enabled PyTorch build before running the notebook.

## Run

Open the notebook:

```bash
jupyter notebook notebooks/region_captioning_demo.ipynb
```

Then run the cells from top to bottom.

The notebook:

- creates local `datasets/` and `outputs/` folders,
- tries to download a sample COCO image for testing,
- falls back to `assets/example_input.jpg` if COCO cannot be downloaded,
- loads SAM3, Florence-2, and BLIP,
- saves the selected input, overlay, and crop into `outputs/`.

## Notes

- This repo is intentionally notebook-first and kept minimal.
- Large caches, generated outputs, and model weights should stay out of Git.
- The models are downloaded automatically the first time they are used and are usually stored in the Hugging Face cache under your user profile.
- The notebook has been tested in this repo with the current dependency versions in `requirements.txt`.

# Img Downloader for Website (v0.1)

## Description
This is a simple tool to download images from a website. It supports two modes:
1. Download images via direct links (e.g., 'background.png').
2. Download images by analyzing the image links present on the page.

## Features
- **Download images via link**: If you have a direct link pointing to a page with images, you can download them all into a local folder.
- **Download images from a webpage**: The program scans the content of the page and downloads all images (with extensions `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg`).

## Requirements
Before running the script, ensure you have Python 3.x and the following libraries installed:

- `requests`
- `beautifulsoup4`

You can install them via pip:

```bash
pip install requests beautifulsoup4

echo "Cleaning up directories" 
rm heatmaps/*.png

# echo "Installing dependencies"
# conda install -c r rpy2 cython

echo "Launching notebooks"
jupyter-lab intro.ipynb --port 8008 &

echo "Opening slides"
xdg-open slides.pdf

echo "Done!"

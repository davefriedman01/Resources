# macOS conda env setup
conda create -n pyvizenv python=3.7 anaconda -y
conda activate pyvizenv
pip install python-dotenv
conda install -c anaconda nb_conda -y
conda install -c conda-forge nodejs=10.13 -y
conda install -c pyviz holoviz -y
conda install -c plotly plotly -y
export NODE_OPTIONS=--max-old-space-size=4096
jupyter labextension install @jupyter-widgets/jupyterlab-manager --no-build
jupyter labextension install jupyterlab-plotly --no-build
jupyter labextension install plotlywidget --no-build
jupyter labextension install @pyviz/jupyterlab_pyviz --no-build
jupyter lab build
unset NODE_OPTIONS

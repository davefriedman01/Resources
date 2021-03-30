# CL Command Line



## Resources

[Command Line (Crash Course Computer Science on YouTube)](https://www.youtube.com/watch?v=4RPtJ9UyHS0&feature=emb_title)<br>
[Command Line (freeCodeCamp on YouTube)](https://www.youtube.com/watch?v=yz7nYlnXLfE)<br>
[Command Line (Geek's Lesson on YouTube)](https://www.youtube.com/watch?v=2PGnYjbYuUo)<br>

[Command Line Environment (MIT's Missing Semester)](https://missing.csail.mit.edu/2020/command-line/)<br>
[Editors (Vim) (MIT's Missing Semester)](https://missing.csail.mit.edu/2020/editors/)<br>
[The Shell (MIT's Missing Semester)](https://missing.csail.mit.edu/2020/course-shell/)<br>
[Shell Tools and Scripting (MIT's Missing Semester)](https://missing.csail.mit.edu/2020/shell-tools/)<br>

[Linux Survival](https://linuxsurvival.com)<br>
[Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html)<br>



## Terms

[Autocompletion (Wikipedia)](https://en.wikipedia.org/wiki/Autocomplete)<br>
[Terminal.app (Wikipedia)](https://en.wikipedia.org/wiki/Terminal_(macOS))<br>
[Terminal Emulator (Wikipedia)](https://en.wikipedia.org/wiki/Terminal_emulator)<br>



## Useful Commands

Run these commands in Terminal.app on macOS or in Git Bash on Windows.<br>



#### [Jupyter](https://jupyterlab.readthedocs.io/en/latest/)<br>
`jupyter --version` Verify that Jupyter is successfully installed on your system<br>

`jupyter lab` Open Jupyter in your web browser (Notebooks will be saved in the default directory)<br>
`jupyter lab --notebook-dir=.` Open Jupyter in your web browser (Notebooks will be saved in the current working directory)<br>



#### [Conda](https://conda.io/en/latest/)
[Conda commands for managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)<br>
[Conda command cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)<br>
[Conda command reference](https://docs.conda.io/projects/conda/en/latest/commands.html)<br>

`conda -V` or `conda --version` Verify that conda is successfully installed on your system<br>
`conda info`<br>

**`conda activate dev` Activate the environment called *dev*<br>
`conda deactivate` Deactivate the active environment<br>
`conda list` Check which packages are installed in your current conda environment and their version numbers<br>**

`conda install <package-name>` or `conda install -c conda-forge <package-name>` Install a package<br>

`conda update conda` Update the conda package and environment manager<br>
`conda update anaconda` Update the anaconda meta package<br>

`conda create -n dev python=3.7 anaconda` Create a new environment called *dev* using Python 3.7<br>
`conda search -f python` Check versions of python available to install<br>

`conda env list` List environments<br>
`conda env remove -n dev` Remove the environment called *dev*<br>




#### [Anaconda](https://docs.anaconda.com/anaconda/)
[Anaconda command reference](https://docs.anaconda.com/anacondaorg/commandreference/)<br>

`anaconda -V` or `anaconda --version` Verify that Anaconda is successfully installed on your system<br>



#### SSH Key
`ssh-keygen -t rsa -b 4096 -C <email>` Create a new ssh key<br>
`eval "$(ssh-agent -s)"` Check that the program `ssh-agent` is running on your system by looking for `Agent pid <number>` in the output<br>
`ssh-add ~/.ssh/id_rsa`<br>
`ssh -T git@github.com` Add GitHub to the list of acceptable ssh hosts on your system<br>
`pbcopy < ~/.ssh/id_rsa.pub` Copy the public key to your clipboard in order to paste it in an appropriate place later (macOS)<br>
`clip < ~/.ssh/id_rsa.pub` Copy the public key to your clipboard in order to paste it in an appropriate place later (Windows)<br>



#### [Python](https://www.python.org/doc/)
`python3 --version` Verify that the CPython interpreter is successfully installed on your system (macOS)<br>
`py -3 --version` Verify that the CPython interpreter is successfully installed on your system (Windows)<br>

`python3 --help`<br>
`python3 finance.py` or `python3 -m finance.py` Run a Python script called  _finance.py_<br>
`python3 -c 'from finance import fv; fv();'` Execute a Python function called _fv_ within the module called _finance.py_, directly from the command line<br>



#### [VS Code](https://code.visualstudio.com/docs)
`code --version` Verify that VS Code is successfully installed on your system<br>
`code .` Launch VS Code from the current working directory<br>
[VS Code CLI](https://code.visualstudio.com/docs/editor/command-line)<br>
[VS Code Terminal](https://code.visualstudio.com/docs/editor/integrated-terminal)<br>
[Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)<br>



#### [Homebrew](https://brew.sh) (macOS)
`brew upgrade && brew update && brew cleanup && brew doctor`<br>
or separately:<br>
`brew upgrade`<br>
`brew update`<br>
`brew cleanup`<br>
`brew doctor`<br>



#### System
`systeminfo` General system settings (Windows)<br>
`sysctl -a | grep machdep.cpu.features` Verify that your system is virtualization-capable by looking for `VMX` in the output (macOS)<br>

`which <program>` Check which \<program\> installation is currently set as the default on your system (macOS)<br>
`where <program>` Check which \<program\> installation is currently set as the default on your system (Windows)<br>



## Installation

[Anaconda](https://docs.anaconda.com/anaconda/install/)
for
[macOS](https://docs.anaconda.com/anaconda/install/mac-os/)
and
[Windows](https://docs.anaconda.com/anaconda/install/windows/)
([Windows troubleshooting](https://docs.anaconda.com/anaconda/user-guide/faq/#))<br>

[Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
for
[macOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html)
and
[Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)<br>

[Jupyter](https://jupyter.org/install) (Note: Temporarily fall back to [Jupyter online](https://jupyter.org/try) if you're having trouble with your local installation.)<br>

[VS Code](https://code.visualstudio.com/docs/setup/setup-overview)
for
[macOS](https://code.visualstudio.com/docs/setup/mac)
and
[Windows](https://code.visualstudio.com/docs/setup/windows)<br>

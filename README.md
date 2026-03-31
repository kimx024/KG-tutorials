# Knowledge Graphs and Semantic Technologies Course

## Getting started
Each time you do a project in Python, it is highly recommended to create a virtual python environment to keep the base python environment of your system 'clean', and easily allow you to switch version if needed. This time is no different. To prevent issues regarding the installation of python packages, we highly recommend creating a virtual environment of version `3.10.13`. For instructions on how to do this, have a look at popular python environment mangagers such as [conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/), [pyenv](https://github.com/pyenv/pyenv-virtualenv), and [PyFlow](https://github.com/David-OConnor/pyflow#installation). 

Once the virtual environment has been created and activated, the necesary package can be installed using either `$conda install --file requirements.txt` when using conda (you might need to install torch and pykeen separately as they are not found in conda channels), `$pip install -r requirements.txt` for pyenv, or `$pyflow init` for PyFlow. 

To use the newly created virtual python environment in Jupyter Notebook;
- move to the right directory,
- open a terminal,
- activate the virtual environment (i.e. `$conda activate [YOUR_VENV]` or `$pyenv activate [YOUR_VENV]` if you are using conda or pyenv. PyFlow should do this automatically),
- and start a local jupyter server (i.e. `$jupyter notebook`). Instructions on how to access the server should be printed in the terminal.

Feel free to reach out to the TAs if you have any questions!

## Tutorials
part 1: RDF  
Go through the notebook [rdf-tutorial](TutorialAssignments/rdf-tutorial.ipynb)

part 2: RDFS  
Go through the notebook [rdfs-tutorial](TutorialAssignments/rdfs-tutorial.ipynb)

part 3: OWL  
Try out the notebooks [OWL-1-tutorial](TutorialAssignments/OWL-1-tutorial.ipynb) and [OWL-2-tutorial](TutorialAssignments/OWL-2-tutorial.ipynb)

part 4: SPARQL  
Notebook [SPARQL-tutorial](TutorialAssignments/SPARQL-tutorial.ipynb)

part 5: RDFstar  
Notebook [RDFstar-tutorial](ML4KG-tutorial.md)

part 6: Machine Learning over KGs  
Notebook [ML4KG-tutorial](TutorialAssignments/ML4KG-tutorial.ipynb)

part 7: Entity Linking and Relation Extraction  
- [Slides](https://docs.google.com/presentation/d/1wtjZ40dJqWiKyxgsJgApVtcjN_1567MF6RNXHL4eg-s/edit?usp=sharing)
- [Google Colab notebook - 1 ](https://colab.research.google.com/drive/1-JDcOIHeWDd0Wj21RjtcUgEyOayUjiNf?usp=sharing)
- [Google Colab notebook - 2 ](https://colab.research.google.com/drive/1VXj67yQA0xr2_FGfLdcgRsq3f99iTUHb?usp=sharing)


The ./data/ingredients.rdf and ./data/recipes.rdf are based on the github repo: https://github.com/foodkg/foodkg.github.io.git

The ./data/musicoset_metadata/ files are downloaded from: https://marianaossilva.github.io/DSW2019/#tables


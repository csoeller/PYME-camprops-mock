## PYME-camprops-mock

### A simple mockup to illustrate camera properties via config files

We have a only a few files to quickly generate a mockup:

- camproperties.py - contains dict info from AndorZyla and AndorIxon
- make-yamls.ipynb - lightly wrap these dicts and generate yaml from that simple structure
- AndorsCMOScams.yaml - yaml generated for sCMOS cams
- IXONcams.yaml - yaml generated for Andor IXON emCCDs
- camproperties.ipynb - notebook that mocks up the functionality

The emphasis has here been on keeping it simple but functional, in hopefully keeping with the PYMEconfig idea of a simple implementation


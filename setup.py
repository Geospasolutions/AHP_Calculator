from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name = 'ahp_calculator',
        version='0.3.0',
        description='AHP is one of the extensively used Multi Criteria Decision Making (MCDM) tool for processing multiple important objectives and weighting the criteria. The AHP allows to assign a priority among various alternatives and integrating multidimensional measures into a single scale of priorities.',
        author='Rohit Gautam, Prashant Thapaliya, Binabh Devkota',
        author_email= 'rowheat02@gmail.com',
        long_description = long_description,
        long_description_content_type="text/markdown",
        url='https://github.com/Geospasolutions/AHP_Calculator/',
        packages=['ahp_calculator'],
        license='LICENSE',
        install_requires=[
            'ipywidgets==7.6.5',
            'numpy==1.20.3'],
        zip_safe = False,)
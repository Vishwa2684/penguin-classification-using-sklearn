from setuptools import setup, find_packages

setup(
    name='penguin_classification_model',
    version='1.0',
    author='Vishwa',
    description="This is the ML model i prepared for classification of type of penguin based on 4 input fields which are Culmen Length (mm), Culmen Depth (mm), Flipper Length (mm), Body Mass (g), Sex",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        # Add any other dependencies here
    ],
)
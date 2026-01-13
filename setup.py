from setuptools import setup, find_packages

setup(
    name="meupia-ia",
    version="0.1.0",
    description="Plugin oficial de Inteligência Artificial para o compilador meuPiá",
    author="Henry Hamon",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "pandas",
        "numpy",
        "joblib",
        "meupia-core"
    ],
)

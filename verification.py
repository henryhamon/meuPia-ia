import sys
import os
import numpy as np

# Ensure we can import from the current directory
sys.path.append(os.getcwd())

# Simulate "usar 'ia'" -> "from meupia_ia import *" (if core does "from meupia_ia import *")
from meupia_ia import (
    ia_definir_dados, 
    ia_criar_modelo, 
    ia_treinar, 
    ia_prever, 
    ia_salvar, 
    ia_carregar,
    ia_coletar_amostra,
    ia_exportar_csv,
    _manager
)

def test_plugin_logic():
    print("--- Testing meuPia-ia Plugin Logic ---")

    # 1. Test Data Definition
    X = [[0, 0], [1, 1], [2, 2], [3, 3]]
    y = [0, 10, 20, 30] # Linear relation y = 10x
    ia_definir_dados(X, y)
    
    if _manager.X is not None and _manager.y is not None:
        print("PASS: Data defined.")
    else:
        print("FAIL: Data not defined.")

    # 2. Test Model Creation (Linear Regression)
    ia_criar_modelo("regressao_linear")
    if _manager.model_type == "regressao_linear":
        print("PASS: Model created.")
    else:
        print("FAIL: Model creation failed.")

    # 3. Test Training
    ia_treinar(0.2)
    # Check if model is fitted (simple check: try predict)
    
    # 4. Test Prediction
    pred = ia_prever([4, 4])
    print(f"Prediction for [4,4] (Expected ~40): {pred}")
    if 39.0 < pred < 41.0:
        print("PASS: Prediction accurate.")
    else:
        print("FAIL: Prediction inaccurate.")

    # 5. Test Persistence
    ia_salvar("test_model.pkl")
    if os.path.exists("test_model.pkl"):
        print("PASS: Model saved.")
    else:
        print("FAIL: Model not saved.")
        
    # Reset and Load
    _manager.reset()
    ia_carregar("test_model.pkl")
    if _manager.model is not None:
        print("PASS: Model loaded.")
    else:
        print("FAIL: Model not loaded.")
        
    # 6. Test Data Collection
    ia_coletar_amostra([10, 100])
    ia_coletar_amostra([20, 200])
    ia_exportar_csv("test_data.csv")
    if os.path.exists("test_data.csv"):
        print("PASS: CSV exported.")
    else:
        print("FAIL: CSV not exported.")

    # Cleanup
    if os.path.exists("test_model.pkl"):
        os.remove("test_model.pkl")
    if os.path.exists("test_data.csv"):
        os.remove("test_data.csv")

if __name__ == "__main__":
    test_plugin_logic()

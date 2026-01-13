import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

class IAManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IAManager, cls).__new__(cls)
            cls._instance.X = None
            cls._instance.y = None
            cls._instance.buffer_data = [] # List of dicts or lists for collection
            cls._instance.model = None
            cls._instance.model_type = None
        return cls._instance

    def reset(self):
        self.X = None
        self.y = None
        self.buffer_data = []
        self.model = None

# Global instance
_manager = IAManager()

# --- Wrapper Functions ---

def ia_definir_dados(x_list, y_list):
    """
    Converts Portugol lists (likely list of lists for X, list for y) 
    to numpy arrays/DataFrames.
    """
    try:
        _manager.X = np.array(x_list)
        _manager.y = np.array(y_list)
        print(f"[IA] Dados definidos: {_manager.X.shape[0]} amostras.")
    except Exception as e:
        print(f"[IA] Erro ao definir dados: {e}")

def ia_criar_modelo(tipo_string):
    """
    Instantiates the model based on the string key.
    """
    tipo = tipo_string.lower()
    if tipo == "regressao_linear":
        _manager.model = LinearRegression()
    elif tipo == "arvore":
        _manager.model = DecisionTreeRegressor()
    elif tipo == "floresta":
        _manager.model = RandomForestRegressor()
    elif tipo == "svr":
        _manager.model = SVR()
    elif tipo == "gradient_boosting":
        _manager.model = GradientBoostingRegressor()
    elif tipo == "knn_classificador":
        _manager.model = KNeighborsClassifier()
    else:
        print(f"[IA] Erro: Tipo de modelo desconhecido '{tipo_string}'.")
        return
    
    _manager.model_type = tipo
    print(f"[IA] Modelo '{tipo_string}' criado.")

def ia_treinar(test_size):
    """
    Performs train_test_split, trains the model, and prints the Score/Accuracy.
    test_size: float (0.0 to 1.0)
    """
    if _manager.model is None:
        print("[IA] Erro: Modelo não criado. Use ia_criar_modelo().")
        return
    if _manager.X is None or _manager.y is None:
        print("[IA] Erro: Dados não definidos. Use ia_definir_dados().")
        return

    try:
        X_train, X_test, y_train, y_test = train_test_split(
            _manager.X, _manager.y, test_size=test_size, random_state=42
        )
        
        _manager.model.fit(X_train, y_train)
        score = _manager.model.score(X_test, y_test)
        
        print(f"[IA] Treinamento concluído. Score (R^2 ou Acurácia): {score:.4f}")
    except Exception as e:
        print(f"[IA] Erro durante o treinamento: {e}")

def ia_prever(input_list):
    """
    Returns a single prediction value.
    input_list: list representing a single sample's features.
    """
    if _manager.model is None:
        print("[IA] Erro: Modelo não existe.")
        return 0.0

    try:
        # Reshape to (1, -1) because it's a single sample
        sample = np.array(input_list).reshape(1, -1)
        prediction = _manager.model.predict(sample)
        return float(prediction[0])
    except Exception as e:
        print(f"[IA] Erro na previsão: {e}")
        return 0.0

def ia_salvar(filename):
    """
    Uses joblib for persistence.
    """
    if _manager.model is None:
        print("[IA] Erro: Nenhum modelo para salvar.")
        return
    try:
        joblib.dump(_manager.model, filename)
        print(f"[IA] Modelo salvo em '{filename}'.")
    except Exception as e:
        print(f"[IA] Erro ao salvar modelo: {e}")

def ia_carregar(filename):
    """
    Uses joblib to load a model.
    """
    try:
        _manager.model = joblib.load(filename)
        print(f"[IA] Modelo carregado de '{filename}'.")
    except Exception as e:
        print(f"[IA] Erro ao carregar modelo: {e}")

# --- Data Collection Helpers ---

def ia_coletar_amostra(features):
    """
    Appends a row to a temporary buffer.
    features: list
    """
    _manager.buffer_data.append(features)

def ia_exportar_csv(filename):
    """
    Saves the buffer to CSV.
    """
    try:
        if not _manager.buffer_data:
            print("[IA] Aviso: Buffer vazio, nada para exportar.")
            return
        
        df = pd.DataFrame(_manager.buffer_data)
        # Using simple numeric columns if no headers provided, or we could accept headers
        df.to_csv(filename, index=False, header=False)
        print(f"[IA] Buffer ({len(_manager.buffer_data)} linhas) exportado para '{filename}'.")
    except Exception as e:
        print(f"[IA] Erro ao exportar CSV: {e}")

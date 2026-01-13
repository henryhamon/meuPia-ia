from meupia.analyzers.code_generator import CodeGenerator

class CompilerExtension(CodeGenerator):
    def __init__(self, output_path="output.py"):
        super().__init__(output_path)

    def generate(self, syntax_tree):
        """
        Overrides the base generation to inject the IA plugin import.
        """
        # We define a custom header injection
        custom_header = "from meupia_ia.plugin_ia import *"
        
        # We can append it to the internal buffer or manage it via the result string
        # Assuming the base class might have a method or we simply prepend to the result
        # if we were rewriting the whole method. 
        # However, a cleaner way if strictly inheriting is to rely on how base 'generate' works.
        # If 'generate' returns the string, we can prepend. 
        # If 'generate' writes to file, we might need to intercept.
        
        # Given the prompt says "Override generate header to inject...", 
        # let's assume we call super().generate() and modify the result 
        # OR we inject it into the imports list if the base class supports it.
        
        # Strategy: Prepend to the generated source.
        # Note: This depends heavily on CodeGenerator implementation details not visible here.
        # Assuming generate returns the code string or writes it. 
        
        # Let's try to inspect the base class if we could, but we can't. 
        # So we'll assume a standard string return or file write. 
        # For safety/demonstration, let's assume we want to ensure the import is present at the top.
        
        python_code = super().generate(syntax_tree)
        
        # Inject just after other imports if possible, or at very top (but after standard imports)
        # For simplicity, we prepend it.
        
        if python_code:
            return f"{custom_header}\n{python_code}"
        return python_code

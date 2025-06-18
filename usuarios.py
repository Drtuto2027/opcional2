
class Usuario:
   
    def __init__(self,  nombre, edad,correo):
       
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        
    def validar_usuario(self,mombre,edad,correo):
        
        try:
            query = '''
                INSERT INTO usuarios ( nombre,nombre,correo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            params = (self.nombre) 
                     
            
            result = db.execute_query(query, params)
            return result > 0
            
        except Exception as e:
            print(f"NombreInvalidoError: si el nombre contiene números o símbolos: {e}")
            return False
    
        try:
            query = '''
                INSERT INTO usuarios ( nombre,nombre,correo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            params = (self.nombre) 
                     
            
            result = db.execute_query(query, params)
            return result > 0
            
        except Exception as e:
            print(f"EdadInvalidaError: si la edad no es un número entero entre 0 y 120: {e}")
            return False
    
        try:
            query = '''
                INSERT INTO usuarios ( nombre,nombre,correo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            params = (self.nombre) 
                     
            
            result = db.execute_query(query, params)
            return result > 0
            
        except Exception as e:
            print(f"CorreoInvalidoError: si el correo no contiene "@" o tiene espacios.: {e}")
            return False  
        
        
print ("el usuario debe  ingresar nombre, edad y correo")        
        
        
        
        
        
        
    
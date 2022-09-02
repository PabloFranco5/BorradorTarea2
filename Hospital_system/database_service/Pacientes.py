class PacienteDatabase:
    #creamos un atributo para alojar el nombre de la base de datos
    def __init__(self, database_name) :
        self.database_name = database_name
    #guardamos los datos en un diccionario 
        self.data ={}
    #creamos un contador para todos los posibles registros de los pacientes, el 
    #contador comienza en cero y a medida que llegan pacientes a la clinica el 
    #contador aumenta
        self.id_counter = 0

#con la clase PacienteDatabse vamos a poder crear un registro de un paciente, leer
# el registro creado , actualizarlo o eliminarlo si es necesario 

#Metodo para crear un dato: 

    def create(self, data: dict) -> int:
        """"
        Este método agrega un registro en la base de datos y retorna el ID asociado
        
        Parámetros
        ----------
        data: dict
            Datos asociados a un estudiante

        Returns
        -------
        out: int
            ID of the student
        """
        self.data[self.id_counter] = data
        self.id_counter += 1

        return self.id_counter - 1

    #def create(self, data): 
        #cada vez que registramos un paciente, actualizamos el 
        #contador de registros de los pacientes
        #self.data[self.id_counter] = data
        #self.id_counter += 1

        #vamos a ver que id uso 
        #return self.id_counter -1
        

#Metodo para leer los datos asociados al paciente:

    def read(self,_id):
        # lo que hacemos es que con el diccionario de datos y retornamos 
        # los datos del paciente asociados al id de identificacion 
        return self.data[_id] 
        

#Metodo para actualizar los datos de un paciente asociado al diccionario:

    def update(self, _id, data):
        # lo que hacemos es leer el id correspondiente del paciente y poner 
        # los nuevos datos en dicho id
        self.data[_id] = data

#Metodo para borrar los datos del paciente asociados al diccionario:


    def delete(self,_id):
        #borramos al paciente con sus datos correspondientes
        del self.data[_id]


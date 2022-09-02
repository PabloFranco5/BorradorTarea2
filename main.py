from argparse import ArgumentParser, Namespace


#importamos el servicio de base de datos de los pacientes
from Hospital_system.database_service.Pacientes import PacienteDatabase

class PacientesDatabase(PacienteDatabase):
    def __init__(self):
        super().__init__(database_name="Pacientes")


def execute(args):
    database = None
    if args.database_name == "Pacientes":
        database = PacientesDatabase()


    while True:
        # Para el registro de la historia clinica vamos a pedirle 
        # Nombre, apellidos, Identificacion, Numero de contacto, Nombre 
        # de la EPS a la que esta afiliado
        user_input = input("Ingrese los datos del paciente: ")

        nombre, apellidos, identificacion, Eps, contacto, sangre, edad =user_input.split(" ")

        #vamos a hacer el metodo de create
        Paciente_id = database.create( {
            "nombre" : nombre,
            "apellidos" : apellidos,
            "identificacion" : identificacion,
            "Eps": Eps,
            "numero_de_contacto" : contacto,
            "tipo_de_sangre" :sangre,
            "edad": edad
            })

        print(database.read(Paciente_id))



def main():
    parser = ArgumentParser()
    parser.add_argument( 
        "-dn","--database-name", type=str, 
        choices=["Pacientes","doctores", "others"]
    )

    args = parser.parse_args()
    execute(args)

if __name__ == "__main__":
    main()
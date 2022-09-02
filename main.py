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
        # Para el registro de la historia clinica vamos a pedirle:

        user_input = input("Ingrese los datos del paciente: ")

        nombre, apellidos, identificacion, Eps, contacto, sangre, edad, direccion, antecedentes, problema, medico, documento, observaciones, cuidados, evolucion, responsable, quirurgica, alta  =user_input.split(" ")

        #vamos a hacer el metodo de create
        Paciente_id = database.create( {
            "nombre_del_paciente" : str(nombre),
            "apellidos_del_paciente" : str(apellidos),
            "identificacion_del_paciente" : int(identificacion),
            "Eps_que_lo_cubre": int(Eps),
            "numero_de_contacto" : int(contacto),
            "tipo_de_sangre" : sangre,
            "edad_": int(edad),
            "direccion_de_residencia": str(direccion),
            "antecedentes_de_interes_del_paciente": str(antecedentes),
            "descripcion_del_problema": str(problema), 
            "nombre_del_medico_que_lo_atendio":str(medico),
            "identificacion_profesional": int(documento),
            "observaciones": str(observaciones),
            "planificacion_de_cuidados": str(cuidados),
            "evolucion_del_paciente": str(evolucion),
            "adulto_responsable_en_caso_de_emergencia":str(responsable),
            "informacion_quirurgica": str(quirurgica),
            "informacion_de_alta": str(alta)
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
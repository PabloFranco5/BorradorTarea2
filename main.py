from argparse import ArgumentParser, Namespace
from datetime import date
from unicodedata import east_asian_width


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

        general_input = input("Ingrese el tipo de información al que desea acceder: informacion personal del paciente(p), informacion medica del paciente (m), informacion administrativa del paciente(a), informacion profesional de la salud(s), informacion farmaceutica(f): ")

        identificador = general_input

        if identificador == "p":
            p_input= input("ingrese la informacion personal del paciente, para esto utilice la tecla espacio para la separacion entre campos de datos y use el signo _ para separa hacer separación dentro del campo : tipo_de_documento, número_de_documento, nombres, apellidos, número_de_contacto, ciudad_de_residencia, dirección_de_residencia, estado_civil, nacionalidad, número_de_contacto_de_emergencia, fecha_de_última_actualización : ")
                
            tipodoc, documento, nombre, apellido, contacto, ciudad, direccion, civil, nacionalidad, emergencia, actualizacion =p_input.split(" ")

            infopersonal_id= database.create({
                "tipo_de_documento" :  str(tipodoc),
                "número_de_documento": int(documento), 
                "nombres_del_paciente": str(nombre), 
                "apellidos_del_paciente": str(apellido), 
                "número_de_contacto": int(contacto), 
                "ciudad_de_residencia": str(ciudad), 
                "dirección_de_residencia": str(direccion), 
                "estado_civil": str(civil), 
                "nacionalidad": str(nacionalidad),
                "número_de_contacto_de_emergencia": int(emergencia), 
                "fecha_de_última_actualización": str(actualizacion)})
            
            print(database.read(infopersonal_id))
        
        if identificador == "m":
            m_input=input("ingrese la informacion medica del paciente: para esto utilice la tecla espacio para la separacion entre campos de datos y use el signo _ para separa hacer separación dentro del campo : tipo_de_documento, numero_de_documento, numero_historia_clinica, edad, sexo, RH, grupo_sangineo, peso, estatura, consentimiento_reanimación, alergias, enfermedades_de_base, cant_embarazos, FMU, observaciones_medicas, remision_a_especialista, tipo_de_especialista, medicacion, tipo_de_medicacion, fecha_de_última_actualización: ")
            tipodoc,documento, historia, edad, sexo, RH, sanguineo, peso, estatura, reanimacion, alergias, comorbilidades, embarazos, FUM, observaciones, remision, especialista, medicacion, actualizacion=m_input.split(" ")

            infomedica_id=database.create({
                "tipo_de_documento": str(tipodoc),
                "numero_de_documento": int(documento), 
                "numero_historia_clinica": int(historia), 
                "edad_del_paciente": int(edad), 
                "sexo_del_paciente": str(sexo), 
                "RH": str(RH), 
                "grupo_sanguineo": str(sanguineo), 
                "peso_del_paciente": int(peso), 
                "estatura_del_paciente": int(estatura), 
                "consentimiento_reanimación": str(reanimacion), 
                "alergias": str(alergias), 
                "enfermedades_de_base": str(comorbilidades),
                "cant_embarazos": int(embarazos), 
                "Fecha_de _última_menstruación_(FUM)": str(FUM), 
                "observaciones_medicas": str(observaciones), 
                "remision_a_especialista": str(remision), 
                "tipo_de_especialista": str(especialista), 
                "medicacion_recetada_por_el_doctor": str(medicacion), 
                "fecha_de_última_actualización": str(actualizacion)
            })
            print(database.read(infomedica_id))

        if identificador == "a":
            a_input= input("ingrese la informacion administrativa del paciente, para esto utilice la tecla espacio para la separacion entre campos de datos y use el signo _ para separa hacer separación dentro del campo : número_ticket_atención, número_historia_clínica, número_documento_paciente, id_profesional_médico, eps_paciente, fecha/hora_entrada, fecha/hora_salida, hospitalización, ubicación_hospital, alta_voluntaria: ")
                
            ticket, historia, documento, profesional, eps, entrada, salida, hospitalizacion, ubicacion, alta =a_input.split(" ")

            infoadministrativa_id= database.create({
                "número_ticket_atención" :  str(ticket),
                "número_historia_clínica": int(historia), 
                "número_documento_paciente": int(documento), 
                "id_profesional_médico": str(profesional), 
                "eps_paciente": str(eps), 
                "fecha/hora_entrada": str(entrada), 
                "fecha/hora_salida": str(salida), 
                "hospitalización_o_ambulatorio": str(hospitalizacion), 
                "ubicación_hospital": str(ubicacion),
                "alta_voluntaria": str(alta)})
            
            print(database.read(infoadministrativa_id))
        

        if identificador =="s":
            s_input=input("ingrese los datos del medico responsable, para esto utilice la tecla espacio para la separacion entre campos de datos y use el signo _ para separa hacer separación dentro del campo : nombre_del_profesional, tipo_de_documento, numero_de_documento, numero_tarjeta_profesional, especialidad, numero_de_consultorio: ")

            nombre, tipodoc, documento, tarjetaprof, especialidad, consultorio =s_input.split(" ")

            infoprofesionalsalud_id = database.create({
                "nombre_del_profesional": str(nombre), 
                "tipo_de_documento": str(tipodoc), 
                "numero_de_documento": int(documento), 
                "numero_tarjeta_profesional": int(tarjetaprof), 
                "especialidad": str(especialidad), 
                "numero_de_consultorio": str(consultorio)
            })

            print(database.read(infoprofesionalsalud_id))

        if identificador == "f":
            f_input= input("ingrese la informacion farmacéutica, para esto utilice la tecla espacio para la separacion entre campos de datos y use el signo _ para separa hacer separación dentro del campo : número_ticket_atención, número_documento_paciente, numero_historia_clínica, profesional_farmacéutico, tarjeta_profesional_farmacéutico, nombre_medicamento, laboratorio_medicamento, código_medicamento, vía_administración_medicamento, cantidad, Fecha/hora_entrega: ")
                
            ticket, documento, historia, farmaceuta, profesional, medicamento, laboratorio, codigo, administracion, cantidad, entrega =f_input.split(" ")
            infofarmaceutica_id= database.create({
                "número_ticket_atención" :  str(ticket),
                "número_documento_paciente": int(documento), 
                "número_historia_clínica": int(historia), 
                "profesional_farmacéutico": str(farmaceuta), 
                "tarjeta_profesional_farmacéutico": int(profesional), 
                "nombre_medicamento": str(medicamento), 
                "laboratorio_medicamento": str(laboratorio), 
                "código_medicamento": str(codigo), 
                "vía_administración_medicamento": str(administracion),
                "cantidad": int(cantidad),
                "Fecha/hora_entrega": str(entrega)
                })

            print(database.read(infofarmaceutica_id)) 



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
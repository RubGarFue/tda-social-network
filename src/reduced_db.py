import sql.sql_backend as sql
import distance.top_users as tu
import re

###################################################################################################
#                                                                                                 #
#                                      UTILIZACIÓN DEL SCRIPT                                     #
#                                                                                                 #
###################################################################################################
#                                                                                                 #
# 1. Ejecutar el script con python3 reduced_db.py                                                 #
#    + El script actualizará user.sql y mention.sql (los archvios importantes para las consultas) #
#    + El script irá mostrando el progreso de la ejecución                                        #
#    + Hay que esperar a que termine la ejecución                                                 #
# 2. Editar el archivo user.sql:                                                                  #
#    + Añadir la siguiente linea antes de la inserción de los usuarios: (línea 41)                #
#      INSERT INTO `user` (`id`, `user_id`, `created_at`, `retrieved_at`) VALUES                  #
#    + En la última inserción, quitar ',' y añadir ';'                                            #
# 3. Editar el archivo mention.sql:                                                               #
#    + Abrir el archivo, buscar y eliminar todas las líneas líneas que concuerden con:            #
#      INSERT INTO `mention` (`id`, `tweet_id`, `user_id`, `retrieved_at`) VALUE;                 #
#    + En la última inserción, quitar ',' y añadir ';'                                            #
#                                                                                                 #
###################################################################################################

def main():
    prueba_db = sql.get_engine('phpmyadmin')

    # Obtenemos los top users
    print("Obteniondo top users...")
    top_users = tu.top_users(prueba_db)
    not_delete_users = []
    
    print("Leyendo usuarios...")

    with open('/home/rubgarfue/Descargas/original_db/user.sql') as f:
        # Obtenemos todas las lineas del fichero
        lines = f.readlines()
        delete_lines = []
        for i in range(len(lines)):
            print("Linea " + str(i+1) + "/" + str(len(lines)))
            # Si la linea es la creación de un nuevo usuario
            if re.match(r"^\([0-9]+, ", lines[i]):
                split = lines[i].split(',')
                user = split[1][2:-1]
                # Si el usuario a crear no está en top lo eliminamos
                if user not in top_users:
                    delete_lines.append(i)
                else:
                    not_delete_users.append(split[0][1:])
            elif re.match(r"^INSERT INTO `user`", lines[i]):
                delete_lines.append(i)
        
        print("\nBorrando lineas...")
        delete_len = len(delete_lines)

        # Borramos las lineas indicadas
        write_lines = lines[:delete_lines[0]]
        for i in range(delete_len-1):
            print(str(i+1) + "/" + str(len(delete_lines)) + " borrado")
            write_lines += lines[delete_lines[i]+1:delete_lines[i+1]]
        write_lines += lines[delete_lines[-1]+1:]
    
    print("\n" + str(delete_len) + " lineas borradas\n")
    print("Escribiendo usuarios...")
    
    # Escribimos el nuevo fichero
    with open('/home/rubgarfue/Descargas/reduced_db/user.sql', 'w') as f:
        f.write(''.join(write_lines))
    
    ###############################################################################################

    print("Leyendo mentions...")

    with open('/home/rubgarfue/Descargas/original_db/mention.sql') as f:
        # Obtenemos todas las lineas del fichero
        lines = f.readlines()
        delete_lines = []
        for i in range(len(lines)):
            print("Linea " + str(i+1) + "/" + str(len(lines)))
            # Si la linea es la creación de una nueva mención
            if re.match(r"^\([0-9]+, ", lines[i]):
                user = lines[i].split(',')[2][1:]
                # Si la mencion a crear menciona a un usaurio no creado la eliminamos
                if user not in not_delete_users:
                    delete_lines.append(i)
        
        print("\nBorrando lineas...")
        delete_len = len(delete_lines)

        # Borramos las lineas indicadas
        write_lines = lines[:delete_lines[0]]
        for i in range(delete_len-1):
            print(str(i+1) + "/" + str(len(delete_lines)) + " borrado")
            write_lines += lines[delete_lines[i]+1:delete_lines[i+1]]
        write_lines += lines[delete_lines[-1]+1:]

        print("\nLeyendo líneas de inserción...")
        # Leemos las lineas del texto a escribir
        insert_change = []
        for i in range(len(write_lines)):
            print("Linea " + str(i+1) + "/" + str(len(write_lines)))
            # Si la linea es la inserción de los usuarios la añadimos al cambio
            if re.match(r"^INSERT INTO `mention`", write_lines[i]):
                insert_change.append(i)
        
        print("\nCambiando líneas de inserción...")
        # Cambiamos las líneas de inserción
        insert_change_len = len(insert_change)
        for i in range(1, insert_change_len-1):
            print(str(i) + "/" + str(len(insert_change)))
            write_lines[insert_change[i]-1] = write_lines[insert_change[i]-1][:-2] + ';\n'
    
    print("\n" + str(len(delete_lines)) + " lineas borradas\n")
    print("Escribiendo mentions...")
    
    # Escribimos el nuevo fichero
    with open('/home/rubgarfue/Descargas/reduced_db/mention.sql', 'w') as f:
        f.write(''.join(write_lines))
            

if __name__ == '__main__':
    main()
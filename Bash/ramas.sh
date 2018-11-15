echo -e "\n\033[32m1\e[0m - Bugfix(Arreglo de fallo):
Problemas durante la fase de desarrollo y prueba internamente.\n";
echo -e "\033[32m2\e[0m - Feature(Característica): 
Incorporación de nuevas caracteriscas de algún componente que ya está hecho.\n";
echo -e "\033[32m3\e[0m - Hotfix(Revisión):
Problemas en la versión actual del sistema y 
no se puede esperar a que se solucione hasta la próxima versión.
Estos se tienen que solucionar de forma inmediata.\n";
echo -e "\033[32m4\e[0m - Release(Lanzamiento): 
Incorporación de componente nuevo\n";
echo -e "\033[32m5\e[0m - Otro: 
Descripción del objetivo de la rama\n";
read -p "Introduzca una opción: " opcion

if (($opcion > 5)) || (($opcion <= 0))
    then
        echo -e "\033[31mOpción no valida\e[0m"
        exit 1
    else 
        echo -e "\n"
        read -p "Nombre de la rama (Ej: nombre_rama): " nombreRama
        case $opcion in 
            1)
                ./ramanueva.sh "bugfix_${nombreRama,,}";;
            2)
                ./ramanueva.sh "feature_${nombreRama,,}";;
            3)
                ./ramanueva.sh "hotfix_${nombreRama,,}";;
            4)
                ./ramanueva.sh "release_${nombreRama,,}";;
            5)
                ./ramanueva.sh ${nombreRama,,};;
        esac
fi
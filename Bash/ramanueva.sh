ramaactual=$(git symbolic-ref --short -q HEAD)

if [ -z $1 ]; then
    echo Digita el nombre de una rama
    exit 1;
fi

if git rev-parse --verify --quiet $1
then
   echo "La rama $1 ya existe."
   exit 1
else
    if [ $ramaactual = "master" ]
    then
        git fetch --prune 
        git pull 
        git checkout -b $1 
        git push -u origin $1; 
        echo La rama $1 ha sido creada
        exit 1
    else
        git checkout master
        if [ $? -eq 0 ]; then
            git fetch --prune
            git pull 
            git checkout -b $1 
            git push -u origin $1
            echo La rama $1 ha sido creada
            exit 1
        else
            echo Tenes cambios pendientes
        fi
    fi
fi





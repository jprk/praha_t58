python "%SUMO_HOME%\tools\randomTrips.py" -n palmovka_cakovice.net.xml --fringe-factor 1  -p 0.221725 -o palmovka_cakovice.pedestrian.trips.xml -e 3600 -r palmovka_cakovice.pedestrian.rou.xml --vehicle-class pedestrian --pedestrians --prefix ped --max-distance 2000
python "%SUMO_HOME%\tools\randomTrips.py" -n palmovka_cakovice.net.xml --fringe-factor 2  -p 0.749305 -o palmovka_cakovice.bicycle.trips.xml    -e 3600 --vehicle-class bicycle --vclass bicycle --prefix bike --fringe-start-attributes "departSpeed=\"max\"" --max-distance 8000 --trip-attributes "departLane=\"best\"" --validate
python "%SUMO_HOME%\tools\randomTrips.py" -n palmovka_cakovice.net.xml --fringe-factor 5  -p 0.299727 -o palmovka_cakovice.passenger.trips.xml  -e 3600 -r palmovka_cakovice.passenger.rou.xml --vehicle-class passenger --vclass passenger --prefix veh --min-distance 300 --trip-attributes "departLane=\"best\"" --fringe-start-attributes "departSpeed=\"max\"" --allow-fringe.min-length 1000 --lanes --validate
python "%SUMO_HOME%\tools\randomTrips.py" -n palmovka_cakovice.net.xml --fringe-factor 5  -p 1.998181 -o palmovka_cakovice.truck.trips.xml      -e 3600 --vehicle-class truck --vclass truck --prefix truck --min-distance 600 --fringe-start-attributes "departSpeed=\"max\"" --trip-attributes "departLane=\"best\"" --validate
python "%SUMO_HOME%\tools\randomTrips.py" -n palmovka_cakovice.net.xml --fringe-factor 20 -p 4.762889 -o palmovka_cakovice.bus.trips.xml        -e 3600 --vehicle-class bus --vclass bus --prefix bus --min-distance 600 --fringe-start-attributes "departSpeed=\"max\"" --trip-attributes "departLane=\"best\"" --validate

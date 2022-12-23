def create_data_model():
    """Stores the data for the problem."""

    data = {}

    maxt = 200
    maxb = 30

    # (1) <-> recharge station (4-5) is forbidden
    data['time_matrix'] = [
        [0, 4, 9, 5, maxt, maxt],
        [4, 0, 5, 11, 12, maxt],
        [9, 5, 0, 6, 6, maxt],
        [5, 11, 6, 0, 10, maxt],
        [maxt, maxt, maxt, maxt, 0, 2],
        [maxt, 12, 6, 10, maxt, 0],
    ]

    data['energy_matrix'] = [
        [0, 4, 9, 5, maxb, maxb],
        [4, 0, 5, 11, 12, maxb],
        [9, 5, 0, 6, 6, maxb],
        [5, 11, 6, 0, 3, maxb],
        [maxb, maxb, maxb, maxb, 0, -30],
        [maxb, 12, 6, 3, maxb, 0],
    ]

    data['time_windows'] = [
        (0, 0),  # depot
        (3, maxt),  # 1
        (6, maxt),  # 2
        (10, maxt),  # 3
        (0, maxt),  # 4 charging in
        (0, maxt),  # 5 charging out
    ]

    data['num_vehicles'] = 1

    # battery capacities correspond to maximum energy consumption by the respective ev before it needs to recharge
    data['vehicle_max_time'] = maxt

    data['battery_capacities'] = maxb

    # list of evse locations from the initial matrix, used to generate the modified energy and time matrices with duplicate evse nodes
    data['evse_nodes'] = [
        4
    ]  #Which means that the evse is represented by nodes 8 and 9 in the modified matrix

    # data['demands'] = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]

    data['depot'] = 0

    # [START initial_routes]
    data['initial_routes'] = [
        [1, 2, 4, 5, 3],  # vehicle 0
    ]
    # [END initial_routes]
    return data

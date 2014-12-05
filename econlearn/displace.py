class Displace:

    """
    Optimal displacement vector table, self.table[D][L] D = number of dimensions, L = number of layers
    """

    def __init__(self, ):

        self.table ={ 1 : {
                        2 : [1],
                        3 : [1],
                        4 : [1],
                        5 : [1],
                        6 : [1],
                        7 : [1],
                        8 : [1],
                        9 : [1],
                        10 : [1],
                        11 : [1],
                        12 : [1],
                        13 : [1],
                        14 : [1],
                        15 : [1],
                        16 : [1],
                        17 : [1],
                        18 : [1],
                        19 : [1],
                        20 : [1], 
                        21 : [1],
                        22 : [1],
                        23 : [1],
                        24 : [1],
                        25 : [1],
                        26 : [1],
                        27 : [1],
                        28 : [1],
                        29 : [1],
                        30 : [1],
                        31 : [1],
                        32 : [1],
                        33 : [1],
                        34 : [1],
                        35 : [1],
                        36 : [1],
                        37 : [1],
                        38 : [1],
                        39 : [1],
                        41 : [1],
                        42 : [1],
                        43 : [1],
                        44 : [1],
                        45 : [1],
                        46 : [1],
                        47 : [1],
                        48 : [1],
                        49 : [1],
                        50 : [1], } ,
                    2 : {
                        2 : [1, 1],
                        3 : [1, 1],
                        4 : [1, 1],
                        5 : [1, 2],
                        6 : [1, 1],
                        7 : [1, 2],
                        8 : [1, 3],
                        9 : [1, 2],
                        10 : [1, 3],
                        11 : [1, 3],
                        12 : [1, 5],
                        13 : [1, 5],
                        14 : [1, 3],
                        15 : [1, 4],
                        16 : [1, 3],
                        17 : [1, 4],
                        18 : [1, 5],
                        19 : [1, 4],
                        20 : [1, 3], 
                        21 : [1, 8],
                        22 : [1, 5],
                        23 : [1, 5],
                        24 : [1, 5], 
                        25 : [1, 7], 
                        26 : [1, 5], 
                        27 : [1, 5], 
                        28 : [1, 5], 
                        29 : [1, 12], 
                        30 : [1, 7], 
                        31 : [1, 12], 
                        32 : [1, 7], 
                        33 : [1, 7], 
                        34 : [1, 13], 
                        35 : [1, 6], 
                        36 : [1, 5], 
                        37 : [1, 6], 
                        38 : [1, 7], 
                        39 : [1, 7], 
                        40 : [1, 7],
                        41 : [1, 9], 
                        42 : [1, 5], 
                        43 : [1, 12], 
                        44 : [1, 7], 
                        45 : [1, 19], 
                        46 : [1, 7], 
                        47 : [1, 7], 
                        48 : [1, 7], 
                        49 : [1, 9], 
                        50 : [1, 19],  },
                    3 : {
                        2 : [1, 1, 1],
                        3 : [1, 1, 1],
                        4 : [1, 1, 1],
                        5 : [1, 1, 2],
                        6 : [1, 1, 1],
                        7 : [1, 2, 3],
                        8 : [1, 1, 3],
                        9 : [1, 2, 4],
                        10 : [1, 1, 3],
                        11 : [1, 2, 4],
                        12 : [1, 1, 5],
                        13 : [1, 2, 5],
                        14 : [1, 3, 5],
                        15 : [1, 2, 4],
                        16 : [1, 3, 5],
                        17 : [1, 2, 6],
                        18 : [1, 5, 7],
                        19 : [1, 3, 7],
                        20 : [1, 3, 7], 
                        21 : [1, 2, 8],
                        22 : [1, 3, 7],
                        23 : [1, 3, 8],
                        24 : [1, 5, 7], 
                        25 : [1, 3, 8], 
                        26 : [1, 3, 9], 
                        27 : [1, 4, 10], 
                        28 : [1, 3, 9], 
                        29 : [1, 3, 9], 
                        30 : [1, 7, 11], 
                        31 : [1, 3, 11], 
                        32 : [1, 3, 9], 
                        33 : [1, 4, 10], 
                        34 : [1, 3, 13], 
                        35 : [1, 11 , 16], 
                        36 : [1, 5, 17], 
                        37 : [1, 7, 17], 
                        38 : [1, 7, 11], 
                        39 : [1, 4, 14], 
                        40 : [1, 3, 11],
                        41 : [1, 4, 13], 
                        42 : [1, 5, 13], 
                        43 : [1, 4, 15], 
                        44 : [1, 3, 17], 
                        45 : [1, 4, 17], 
                        46 : [1, 5, 13], 
                        47 : [1, 4, 18], 
                        48 : [1, 5, 17], 
                        49 : [1, 4, 19], 
                        50 : [1, 7, 11],  },
                    4 : {
                        2 : [1, 1, 1, 1],
                        3 : [1, 1, 1, 1],
                        4 : [1, 1, 1, 1],
                        5 : [1, 1, 2, 2],
                        6 : [1, 1, 1, 1],
                        7 : [1, 1, 2, 3],
                        8 : [1, 1, 3, 3],
                        9 : [1, 1, 2, 4],
                        10 : [1, 1, 3, 3],
                        11 : [1, 1, 3, 5],
                        12 : [1, 1, 5, 5],
                        13 : [1, 2, 3, 6],
                        14 : [1, 1, 3, 5],
                        15 : [1, 2, 4, 7],
                        16 : [1, 3, 5, 7],
                        17 : [1, 2, 4, 8],
                        18 : [1, 1, 5, 7],
                        19 : [1, 2, 4, 8],
                        20 : [1, 3, 7, 9], 
                        21 : [1, 2, 5, 8],
                        22 : [1, 3, 5, 7],
                        23 : [1, 2, 6, 10],
                        24 : [1, 5, 7, 11], 
                        25 : [1, 2, 7, 11], 
                        26 : [1, 3, 5, 11], 
                        27 : [1, 2, 5, 10], 
                        28 : [1, 3, 5, 11], 
                        29 : [1, 3, 7, 12], 
                        30 : [1, 7, 11, 13], 
                        31 : [1, 3, 5, 12], 
                        32 : [1, 3, 5, 13], 
                        33 : [1, 2, 8, 14], 
                        34 : [1, 9, 13, 15], 
                        35 : [1, 11, 8, 13], 
                        36 : [1, 5, 7, 17], 
                        37 : [1, 3, 8, 14], 
                        38 : [1, 3, 7, 13], 
                        39 : [1, 4, 10, 16], 
                        40 : [1, 3, 9, 13],
                        41 : [1, 3, 9, 14], 
                        42 : [1, 5, 11, 13], 
                        43 : [1, 3, 13, 19], 
                        44 : [1, 3, 7, 19], 
                        45 : [1, 4, 7, 16], 
                        46 : [1, 3, 7, 19], 
                        47 : [1, 3, 8, 17], 
                        48 : [1, 5, 11, 23], 
                        49 : [1, 3, 8, 18], 
                        50 : [1, 3, 7, 19],  },
                    5 : {
                        2 : [1, 1, 1, 1, 1],
                        3 : [1, 1, 1, 1, 1],
                        4 : [1, 1, 1, 1, 1],
                        5 : [1, 1, 1, 2, 2],
                        6 : [1, 1, 1, 1, 1],
                        7 : [1, 1, 2, 2, 3],
                        8 : [1, 1, 1, 3, 3],
                        9 : [1, 1, 2, 2, 4],
                        10 : [1, 1, 1, 3, 3],
                        11 : [1, 2, 3, 4, 5],
                        12 : [1, 1, 1, 5, 5],
                        13 : [1, 2, 3, 4, 5],
                        14 : [1, 1, 3, 3, 5],
                        15 : [1, 1, 2, 4, 7],
                        16 : [1, 1, 3, 5, 7],
                        17 : [1, 2, 3, 4, 8],
                        18 : [1, 1, 5, 5, 7],
                        19 : [1, 2, 3, 5, 9],
                        20 : [1, 1, 3, 7, 9], 
                        21 : [1, 1, 5, 8, 10],
                        22 : [1, 3, 5, 7, 9],
                        23 : [1, 2, 4, 7, 10],
                        24 : [1, 1, 5, 7, 11], 
                        25 : [1, 2, 3, 7, 11], 
                        26 : [1, 3, 5, 7, 9], 
                        27 : [1, 2, 4, 7, 13], 
                        28 : [1, 3, 5, 9, 11], 
                        29 : [1, 2, 4, 7, 13], 
                        30 : [1, 1, 7, 11, 13], 
                        31 : [1, 2, 4, 8, 15], 
                        32 : [1, 3, 5, 7, 13], 
                        33 : [1, 2, 4, 8, 16], 
                        34 : [1, 3, 5, 7, 15], 
                        35 : [1, 2, 4, 9, 16], 
                        36 : [1, 5, 7, 11, 13], 
                        37 : [1, 2, 5, 9, 17], 
                        38 : [1, 3, 5, 7, 17], 
                        39 : [1, 2, 4, 10, 17], 
                        40 : [1, 3, 7, 9, 19],
                        41 : [1, 4, 10, 16, 18], 
                        42 : [1, 5, 11, 13, 17], 
                        43 : [1, 2, 6, 10, 20], 
                        44 : [1, 5, 7, 9, 19], 
                        45 : [1, 2, 4, 11, 19], 
                        46 : [1, 3, 5, 11, 21], 
                        47 : [1, 2, 6, 10, 22], 
                        48 : [1, 5, 7, 11, 23], 
                        49 : [1, 2, 5, 12, 20], 
                        50 : [1, 3, 11, 13, 19],  },
                    6 : {
                        2 : [1, 1, 1, 1, 1, 1],
                        3 : [1, 1, 1, 1, 1, 1],
                        4 : [1, 1, 1, 1, 1, 1],
                        5 : [1, 1, 1, 2, 2, 2],
                        6 : [1, 1, 1, 1, 1, 1],
                        7 : [1, 1, 2, 2, 3, 3],
                        8 : [1, 1, 1, 3, 3, 3],
                        9 : [1, 1, 2, 2, 4, 4],
                        10 : [1, 1, 1, 3, 3, 3],
                        11 : [1, 1, 2, 3, 4, 5],
                        12 : [1, 1, 1, 5, 5, 5],
                        13 : [1, 2, 3, 4, 5, 6],
                        14 : [1, 1, 3, 3, 5, 5],
                        15 : [1, 1, 2, 4, 7, 7],
                        16 : [1, 1, 3, 3, 5, 7],
                        17 : [1, 2, 3, 4, 6, 8],
                        18 : [1, 1, 5, 5, 7, 7],
                        19 : [1, 2, 3, 5, 7, 8],
                        20 : [1, 1, 3, 3, 7, 9], 
                        21 : [1, 2, 4, 5, 8, 10],
                        22 : [1, 1, 3, 5, 7, 9],
                        23 : [1, 2, 3, 6, 7, 11],
                        24 : [1, 1, 5, 7, 11, 11], 
                        25 : [1, 2, 3, 6, 8, 12], 
                        26 : [1, 3, 5, 7, 9, 11], 
                        27 : [1, 2, 4, 5, 7, 13], 
                        28 : [1, 3, 5, 9, 11, 13], 
                        29 : [1, 2, 5, 8, 9, 12], 
                        30 : [1, 1, 7, 7, 11, 13], 
                        31 : [1, 2, 4, 7, 10, 15], 
                        32 : [1, 3, 5, 7, 9, 15], 
                        33 : [1, 1, 5, 7, 10, 14], 
                        34 : [1, 3, 5, 7, 9, 15], 
                        35 : [1, 2, 4, 8, 11, 17], 
                        36 : [1, 5, 7, 11, 13, 17], 
                        37 : [1, 6, 8, 10, 11, 14], 
                        38 : [1, 3, 5, 7, 11, 17], 
                        39 : [1, 2, 4, 8, 11, 17], 
                        40 : [1, 3, 7, 9, 11, 17],
                        41 : [1, 2, 6, 9, 13, 18], 
                        42 : [1, 5, 11, 13, 17, 19], 
                        43 : [1, 2, 7, 11, 15, 20], 
                        44 : [1, 3, 5, 7, 9, 21], 
                        45 : [1, 2, 8, 11, 13, 17], 
                        46 : [1, 3, 5, 11, 17, 21], 
                        47 : [1, 2, 4, 11, 17, 22], 
                        48 : [1, 5, 7, 11, 13, 23], 
                        49 : [1, 2, 6, 10, 13, 22], 
                        50 : [1, 3, 7, 11, 21, 23],  },

                }

class Aggregate:
     aggr = [
    {
        '$addFields': {
            'total_cost': {
                '$multiply': [
                    '$cost', '$quantity'
                ]
            }
        }
    }, {
        '$group': {
            '_id': None,
            'total': {
                '$sum': '$total_cost'
            }
        }
    }, {
        '$project': {
            'id': 0
        }
    }
]
    # aggr = [
    #     {
    #         '$addFields': {
    #             'total_amount': {
    #                 '$multiply': [
    #                     '$quantity', '$cost'
    #                 ]
    #             }
    #         }
    #     }, {
    #         '$group': {
    #             '_id': None,
    #             'total': {
    #                 '$sum': '$total_amount'
    #             }
    #         }
    #     }, {
    #         '$project': {
    #             '_id': 0
    #         }
    #     }
    # ]



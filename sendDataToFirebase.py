# -*- coding: utf-8 -*-

import connector

name = 'SKS'
desc = 'SKS WAR'
price = '50'
quantity = '500'
row = '21'

users_ref = ref
users_ref.update({
    row : {
        'name' : name,
        'desc' : desc,
        'price' : price,
        'quantity' : quantity
    }
})
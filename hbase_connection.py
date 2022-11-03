import happybase

### establish connection between Python and Happybase
connection = happybase.Connection('192.168.56.102')


#### create table

connection.create_table(
    'customer',
    {'address': dict(),
     'order': dict(),
    }
)

table = connection.table('customer')

print(connection.tables())

#### insert data into the table

table.put(b'sathish', {b'address:state': b'Tamil Nadu',
                       b'address:city': b'Tiruttani',
                       b'order:order-id': b'ord-1',
                       b'order:product_name': b'smartphone'})

### Scan table
for key, data in table.scan():
    print(key, data)

### Get table values
row = table.row(b'sathish')
print(row[b'address:state'])

### Delete specific column in a row
table.delete(b'sathish', columns=[b'address:state', b'order:order-id'])

### Delete row in the table
table.delete(b'sathish')

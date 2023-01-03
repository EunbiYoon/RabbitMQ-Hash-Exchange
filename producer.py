import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare('samplehashing', 'x-consistent-hash')

message = 'Hello hash the routing key and pass me on please!'

routing_key_to_hash = '1111111dddd131545654522334455hash m111eeee1111111eee!'

channel.basic_publish(exchange='samplehashing', routing_key=routing_key_to_hash, body=message)

print(f'sent message: {message}')

connection.close()
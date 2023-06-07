import grpc from 'k6/net/grpc'
import { sleep, check } from 'k6'

const client = new grpc.Client()
client.load([], './Helloworld.proto')

export const options = {
    vus: 10,
    duration: "30s",
  };

export default function () {
    client.connect('localhost:3000', { 
        plaintext: true 
    })
    

    const data = { name: 'Bert' }
    const response = client.invoke('helloworld.Greeter/SayHello', data)
    check(response, {
        'status is OK': (r) => r && r.status === grpc.StatusOK,
    })
    console.log(JSON.stringify(response.message))
}

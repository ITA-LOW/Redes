# T1_redes

## Primeiro teste se o servidor ta dando protected
        curl -i http://localhost:5000/protected

## Vai dar erro, agora crie um usuário
        curl -X POST -H "Content-Type: application/json" -d '{"username":"teste", "password":"teste"}' -i http://localhost:5000/register

## Agora, faça o login
        curl -X POST -H "Content-Type: application/json" -d '{"username":"teste", "password":"teste"}' -i http://localhost:5000/login

## Com o token, rode:
        curl -X GET -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InRlc3RlIn0.qkeHntFl8-u2AoVZyydJ0bvGTQZFI91nGJjMTFizYsQ" http://localhost:5000/protected




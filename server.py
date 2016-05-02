import sys
import json

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from games.tictactoe import TicTacToe
from games.scrabble import Scrabble
from games.player import Player


@Request.application
def application(request):

    # default status dispatch method (returns "OK")
    dispatcher["Status.Ping"] = lambda: "OK"

    # if we pass in the arg "tictactoe" then we know to accept tictactoe messages
    if sys.argv[1] == "tictactoe":  

        if json.loads(request.data)['params'] is not None:
            jsonLoad = json.loads(request.data)
            gamestate = jsonLoad['params']['gamestate']

        dispatcher["TicTacToe.Error"] = TicTacToe.Error
        dispatcher["TicTacToe.NextMove"] = TicTacToe.NextMove
        dispatcher["TicTacToe.Complete"] = TicTacToe.Complete
    elif sys.argv[1] == 'scrabble':
        s = Scrabble()
        dispatcher["Scrabble.Ping"] = Scrabble.Ping
        pass
        #todo - put scrabble functions in here

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    try:
        p = Player(str(sys.argv[1]))
        run_simple('0.0.0.0', 8080, application)
        #run_simple('localhost', 8080, application)
    except IndexError as err: 
       print 'Please enter the name of the game to play (tictactoe, snap etc)'

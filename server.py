import sys
import json

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from games.tictactoe import TicTacToe
from games.player import Player


@Request.application
def application(request):

    # default status dispatch method (returns "OK")
    dispatcher["Status.Ping"] = lambda: "OK"

    # if we pass in the arg "tictactoe" then we know to accept tictactoe messages
    if sys.argv[1] == "tictactoe":  
        t = TicTacToe()
        dispatcher["TicTacToe.Error"] = TicTacToe.Error
        dispatcher["TicTacToe.NextMove"] = TicTacToe.NextMove
        dispatcher["TicTacToe.Complete"] = TicTacToe.Complete

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    try:
        p = Player(str(sys.argv[1]))
        run_simple('0.0.0.0', 8080, application)
    except IndexError as err: 
       print 'Please enter the name of the game to play (tictactoe, snap etc)'

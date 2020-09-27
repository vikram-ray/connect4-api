from rest_framework import viewsets, status
from rest_framework.response import Response

from .utils import check_winner

def reset_game(request):
    request.session["player"] = "Yellow"
    request.session['moves'] = []
    board = [["" for i in range(6)] for j in range(7)]
    request.session["board"] = board
    return True

def turn_toggler(request, col):
    new_player = "Yellow" if request.session.get("player") == "Red" else "Red"
    request.session['player'] = new_player
    request.session['moves'].append([new_player, col])

def player_turn(request, col):
    board = request.session.get("board")
    try:
        empty_idx = board[col].index("")
        if empty_idx < 6:
            board[col][empty_idx] = request.session.get("player")
        winner = check_winner(board)
        if winner != "":
            return winner
        turn_toggler(request, col)
        
    except Exception as error:
        print(str(error))
        return False

class Connect4ViewSet(viewsets.ViewSet):

    def create(self, request):
        if request.data.get("action") == "START":
            reset_game(request)
            return Response("READY")

        if request.data.get("column") in range(7):
            result = player_turn(request, request.data.get("column"))
            if result is None:
                return Response("{}'s turn".format(request.session.get("player")))
            if result:
                return Response("{} Wins".format(result))
        return Response("Invalid move",status=status.HTTP_400_BAD_REQUEST)
        

class Connect4MovesViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response(request.session.get("moves"))

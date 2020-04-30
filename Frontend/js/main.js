eel.expose(jswrap)
function jswrap(board){
    document.getElementById('check').setAttribute('onclick', 'check(['+board+'])');
    document.getElementById('solve').setAttribute('onclick', 'solve(['+board+'])');
}


eel.expose(setup);
function setup(position, value) {
    document.getElementById('box'+position).innerHTML = value;
}

function check(board){
    eel.check(board)(checkWithSolvedBoard)
}
function checkWithSolvedBoard(solved){
    list = solved;
    position = 1;
    for (number of solved){

        try{
            elem = document.getElementById('box'+position).children[0].nodeName;
        }
        catch(err){
            elem = 0
        }
        if (elem == 'INPUT'){
            value = document.getElementById('box'+position+'inner').value;
            if (number == value) {
                document.getElementById('box'+position+'inner').classList.add("right");
            }
            else {
                document.getElementById('box'+position+'inner').classList.add("wrong");
            }
        }
        ++position
    }
}
function solve(board){
    eel.solveWithDisplay(board);
    document.getElementById('time').id = 'nottime'
}

